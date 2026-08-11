"""
Extraction pipeline service.

SP-430.4.1 / MF-440.2 / MF-512.4.3-C / SP-440.3.2

Connects routed opportunity artifacts to specialized extractors
and carries extractor decision intelligence into execution.

This version introduces a parallel canonical dispatcher that emits
EvidencePayload objects while preserving the legacy process() API.
"""

from __future__ import annotations

from pathlib import Path

from meridianforge.extraction.identity_extractor import IdentityEvidence
from meridianforge.extractors.inventory_workbook_extractor import (
    InventoryWorkbookExtractor,
)
from meridianforge.extractors.rental_acquisition_extractor import (
    RentalAcquisitionExtractor,
)
from meridianforge.models.domain.evidence_payload import EvidencePayload
from meridianforge.models.domain.extractor_decision_context import (
    ExtractorDecisionContext,
)
from meridianforge.services.evidence_payload_builder import (
    EvidencePayloadBuilder,
)
from meridianforge.services.extraction_audit_service import (
    ExtractionAuditService,
)
from meridianforge.services.opportunity_intake_service import (
    IntakeArtifact,
)
from meridianforge.services.opportunity_mapper import (
    NormalizedRentalOpportunity,
    OpportunityMapper,
)


class ExtractionPipelineService:
    """
    Execute extraction and normalization for routed artifacts.

    Legacy callers continue using process().

    New canonical callers should use process_to_evidence().
    """

    def __init__(
        self,
        audit_service: ExtractionAuditService | None = None,
    ) -> None:
        self._audit = audit_service or ExtractionAuditService()

    # ------------------------------------------------------------------
    # Legacy normalization API
    # ------------------------------------------------------------------

    def process(
        self,
        artifact: IntakeArtifact,
        extractor_name: str | None = None,
        decision_context: ExtractorDecisionContext | None = None,
    ) -> (
        NormalizedRentalOpportunity | dict[str, object] | list[dict[str, object]] | None
    ):
        """
        Execute extraction.

        Supports both legacy extractor routing and MF-440
        decision-context aware execution.
        """

        selected_extractor = extractor_name

        if decision_context is not None:
            selected_extractor = decision_context.selected_extractor

        if selected_extractor == "RentalAcquisitionExtractor":
            rental_record = RentalAcquisitionExtractor.extract(
                text=artifact.extracted_text,
                source_file=Path(artifact.path),
            )

            if rental_record is None:
                return None

            return OpportunityMapper.from_rental_record(
                record=rental_record,
                audit_service=self._audit,
            )

        if selected_extractor == "InventoryWorkbookExtractor":
            records = InventoryWorkbookExtractor.extract(
                Path(artifact.path),
            )

            normalized: list[dict[str, object]] = []

            for inventory_record in records:
                normalized.append(
                    OpportunityMapper.from_inventory_record(
                        record=inventory_record,
                        audit_service=self._audit,
                    )
                )

            return normalized

        return None

    # ------------------------------------------------------------------
    # Canonical evidence API (SP-440.3.2)
    # ------------------------------------------------------------------

    def process_to_evidence(
        self,
        artifact: IntakeArtifact,
        extractor_name: str | None = None,
        decision_context: ExtractorDecisionContext | None = None,
    ) -> EvidencePayload | list[EvidencePayload] | None:
        """
        Execute extraction and return canonical EvidencePayload objects.

        This method intentionally performs extraction only.
        No underwriting or opportunity normalization occurs here.
        """

        selected_extractor = extractor_name

        if decision_context is not None:
            selected_extractor = decision_context.selected_extractor

        if selected_extractor == "RentalAcquisitionExtractor":
            rental_record = RentalAcquisitionExtractor.extract(
                text=artifact.extracted_text,
                source_file=Path(artifact.path),
            )

            if rental_record is None:
                return None

            fields: dict[str, object] = {
                "purchase_price": rental_record.price,
                "monthly_rent": rental_record.rent,
            }

            if rental_record.cash_flow is not None:
                fields["monthly_cash_flow"] = rental_record.cash_flow

            if rental_record.roi is not None:
                fields["cash_on_cash_return"] = rental_record.roi

            identity = IdentityEvidence(
                city=rental_record.city,
                state=rental_record.state,
                confidence=0.99,
            )

            payload = EvidencePayloadBuilder.build(
                fields=fields,
                identity=identity,
                source_file=Path(artifact.path).name,
            )

            payload.source_method = "rental_extractor"
            return payload

        if selected_extractor == "InventoryWorkbookExtractor":
            records = InventoryWorkbookExtractor.extract(
                Path(artifact.path),
            )

            payloads: list[EvidencePayload] = []

            for inventory_record in records:
                fields = {
                    "purchase_price": inventory_record.price,
                    "monthly_cash_flow": inventory_record.cash_flow,
                    "cash_on_cash_return": inventory_record.roi,
                    "initial_cash": inventory_record.initial_cash,
                    "beds": inventory_record.beds,
                    "baths": inventory_record.baths,
                    "year_built": inventory_record.year_built,
                }

                identity = IdentityEvidence(
                    state=inventory_record.state,
                    confidence=0.95,
                )

                payload = EvidencePayloadBuilder.build(
                    fields=fields,
                    identity=identity,
                    source_file=Path(artifact.path).name,
                )

                payload.source_method = "inventory_workbook"
                payloads.append(payload)

            return payloads

        return None
