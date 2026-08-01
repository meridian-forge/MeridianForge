"""
Opportunity normalization mapper.

MF-512.2.3 / MF-512.3.2

Converts classified extraction records into existing MeridianForge
domain models while preserving the distinction between source claims
and MeridianForge validated investment metrics.
"""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal

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
    ) -> NormalizedRentalOpportunity:
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
                    Decimal(str(record.roi))
                    if record.roi is not None
                    else None
                ),
                source_document=str(record.source_file),
            ),
            verified=VerifiedMetrics(),
            decision=DecisionMetrics(),
        )

        return NormalizedRentalOpportunity(
            city=record.city,
            state=record.state,
            acquisition=acquisition,
            monthly_rent=float(record.rent),
            metrics=metrics,
        )
