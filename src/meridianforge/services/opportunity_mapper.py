"""
Opportunity normalization mapper.

MF-512.2.3 / MF-512.3.2 / MF-513.3.1 / MF-512.4.3-B

Converts classified extraction records into existing MeridianForge
domain models while preserving the distinction between source claims
and MeridianForge validated investment metrics.

This milestone also records extraction audit events for every
normalized field flowing into the underwriting pipeline.
"""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal
import re
from typing import Any

from meridianforge.extractors.rental_acquisition_extractor import (
    RentalAcquisitionRecord,
)
from meridianforge.models.domain.acquisition import Acquisition
from meridianforge.models.domain.opportunity_metrics import (
    DecisionMetrics,
    OpportunityMetrics,
    SourceMetrics,
    VerifiedMetrics,
)
from meridianforge.services.extraction_audit_service import (
    ExtractionAuditService,
)


@dataclass(frozen=True)
class NormalizedRentalOpportunity:
    """
    Normalized rental acquisition opportunity.

    Source metrics represent extracted provider claims.
    Verified metrics are populated later by underwriting.
    """

    city: str
    state: str
    acquisition: Acquisition
    monthly_rent: float
    metrics: OpportunityMetrics


class OpportunityMapper:
    """
    Convert extraction records into normalized opportunity objects.
    """

    DEFAULT_CLOSING_COST_RATE = 0.03

    @classmethod
    def from_rental_record(
        cls,
        record: RentalAcquisitionRecord,
        audit_service: ExtractionAuditService | None = None,
    ) -> NormalizedRentalOpportunity:
        audit = audit_service or ExtractionAuditService()

        artifact_id = str(record.source_file)

        closing_costs = round(
            record.price * cls.DEFAULT_CLOSING_COST_RATE,
            2,
        )

        acquisition = Acquisition(
            purchase_price=float(record.price),
            closing_costs=closing_costs,
            rehab_cost=0.0,
        )

        metrics = OpportunityMetrics(
            source=SourceMetrics(
                claimed_purchase_price=Decimal(str(record.price)),
                claimed_rent=Decimal(str(record.rent)),
                claimed_cashflow=(
                    Decimal(str(record.cash_flow))
                    if record.cash_flow is not None
                    else None
                ),
                claimed_roi=(
                    Decimal(str(record.roi)) if record.roi is not None else None
                ),
                source_document=str(record.source_file),
            ),
            verified=VerifiedMetrics(),
            decision=DecisionMetrics(),
        )

        audit.record_field(
            artifact_id=artifact_id,
            source_file=str(record.source_file),
            field_name="purchase_price",
            raw_value=str(record.price),
            normalized_value=str(record.price),
            confidence=0.99,
            extractor="OpportunityMapper",
        )

        audit.record_field(
            artifact_id=artifact_id,
            source_file=str(record.source_file),
            field_name="monthly_rent",
            raw_value=str(record.rent),
            normalized_value=str(record.rent),
            confidence=0.99,
            extractor="OpportunityMapper",
        )

        if record.cash_flow is not None:
            audit.record_field(
                artifact_id=artifact_id,
                source_file=str(record.source_file),
                field_name="cash_flow",
                raw_value=str(record.cash_flow),
                normalized_value=str(record.cash_flow),
                confidence=0.95,
                extractor="OpportunityMapper",
            )

        if record.roi is not None:
            audit.record_field(
                artifact_id=artifact_id,
                source_file=str(record.source_file),
                field_name="roi",
                raw_value=str(record.roi),
                normalized_value=str(record.roi),
                confidence=0.95,
                extractor="OpportunityMapper",
            )

        return NormalizedRentalOpportunity(
            city=record.city,
            state=record.state,
            acquisition=acquisition,
            monthly_rent=float(record.rent),
            metrics=metrics,
        )

    @classmethod
    def from_inventory_record(
        cls,
        record: Any,
        audit_service: ExtractionAuditService | None = None,
    ) -> dict[str, object]:
        """
        Convert an inventory workbook record into the canonical acquisition
        record format expected by AcquisitionExecutionService.

        This intentionally returns a plain dictionary because the acquisition
        pipeline already accepts normalized record dictionaries.
        """

        audit = audit_service or ExtractionAuditService()

        artifact_id = str(record.source_file)

        closing_costs = round(
            float(record.price) * cls.DEFAULT_CLOSING_COST_RATE,
            2,
        )

        city = ""
        zip_code = ""

        address = record.address.strip()

        match = re.match(
            r"^(.*?),\\s*([A-Z]{2})\\s*(\\d{5})",
            address,
        )

        if match:
            city = match.group(1).strip()
            zip_code = match.group(3).strip()

        audit.record_field(
            artifact_id=artifact_id,
            source_file=str(record.source_file),
            field_name="purchase_price",
            raw_value=str(record.price),
            normalized_value=str(record.price),
            confidence=0.99,
            extractor="OpportunityMapper",
        )

        audit.record_field(
            artifact_id=artifact_id,
            source_file=str(record.source_file),
            field_name="roi",
            raw_value=str(record.roi),
            normalized_value=str(record.roi),
            confidence=0.95,
            extractor="OpportunityMapper",
        )

        audit.record_field(
            artifact_id=artifact_id,
            source_file=str(record.source_file),
            field_name="cash_flow",
            raw_value=str(record.cash_flow),
            normalized_value=str(record.cash_flow),
            confidence=0.95,
            extractor="OpportunityMapper",
        )

        return {
            "address": address,
            "city": city,
            "state": record.state,
            "zip_code": zip_code,
            "purchase_price": float(record.price),
            "closing_costs": closing_costs,
            "rehab_cost": 0.0,
            "monthly_rent": 0.0,
            "monthly_cashflow": float(record.cash_flow),
            "projected_roi": float(record.roi),
            "initial_cash": float(record.initial_cash),
            "beds": float(record.beds),
            "baths": float(record.baths),
            "year_built": int(record.year_built),
            "seller_incentives": record.seller_incentives,
            "source": "inventory_workbook",
            "source_document": str(record.source_file),
        }
