"""
Extraction pipeline service.

SP-430.4.1 / MF-440.2

Connects routed opportunity artifacts to specialized extractors
and carries extractor decision intelligence into execution.
"""

from __future__ import annotations

from pathlib import Path

from meridianforge.extractors.rental_acquisition_extractor import (
    RentalAcquisitionExtractor,
)
from meridianforge.models.domain.extractor_decision_context import (
    ExtractorDecisionContext,
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
    """

    def __init__(
        self,
        audit_service: ExtractionAuditService | None = None,
    ) -> None:
        self._audit = audit_service or ExtractionAuditService()

    def process(
        self,
        artifact: IntakeArtifact,
        extractor_name: str | None = None,
        decision_context: ExtractorDecisionContext | None = None,
    ) -> NormalizedRentalOpportunity | None:
        """
        Execute extraction.

        Supports both legacy extractor routing and MF-440
        decision-context aware execution.
        """

        selected_extractor = extractor_name

        if decision_context is not None:
            selected_extractor = decision_context.selected_extractor

        if selected_extractor == "RentalAcquisitionExtractor":
            record = RentalAcquisitionExtractor.extract(
                text=artifact.extracted_text,
                source_file=Path(artifact.path),
            )

            if record is None:
                return None

            return OpportunityMapper.from_rental_record(
                record=record,
                audit_service=self._audit,
            )

        return None
