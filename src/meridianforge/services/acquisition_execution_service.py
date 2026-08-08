"""
Acquisition execution service.

Bridges intake opportunities, extracted normalized opportunities,
and canonical acquisition opportunities into the acquisition pipeline.
"""

from __future__ import annotations

from pathlib import Path

from meridianforge.acquisition.opportunity import (
    Opportunity as AcquisitionOpportunity,
)
from meridianforge.models.domain.investor_profile import (
    InvestorProfile,
)
from meridianforge.models.results.acquisition_orchestration_result import (
    AcquisitionOrchestrationResult,
)
from meridianforge.opportunity.models import (
    Opportunity as IntakeOpportunity,
)
from meridianforge.services.acquisition_orchestrator import (
    AcquisitionOrchestrator,
)
from meridianforge.services.opportunity_mapper import (
    NormalizedRentalOpportunity,
)


class AcquisitionExecutionService:
    """
    Executes acquisition analysis using the canonical
    orchestration pipeline.
    """

    def __init__(
        self,
        orchestrator: AcquisitionOrchestrator | None = None,
    ) -> None:
        self.orchestrator = orchestrator or AcquisitionOrchestrator()

    def execute(
        self,
        opportunity: (
            IntakeOpportunity | AcquisitionOpportunity | NormalizedRentalOpportunity
        ),
        investor_profile: InvestorProfile,
        export_path: Path | None = None,
        archive_path: Path | None = None,
    ) -> AcquisitionOrchestrationResult:
        """
        Execute acquisition analysis from any supported opportunity source.
        """

        record = self._to_record(opportunity)

        return self.orchestrator.analyze(
            [record],
            investor_profile,
            export_path=export_path,
            archive_path=archive_path,
        )

    @staticmethod
    def _to_record(
        opportunity: (
            IntakeOpportunity | AcquisitionOpportunity | NormalizedRentalOpportunity
        ),
    ) -> dict[str, object]:
        """
        Convert supported opportunity models into the normalized
        record format expected by AcquisitionOrchestrator.
        """

        if isinstance(opportunity, dict):
            return opportunity

        if isinstance(opportunity, NormalizedRentalOpportunity):
            source = opportunity.metrics.source

            return {
                "city": opportunity.city,
                "state": opportunity.state,
                "purchase_price": opportunity.acquisition.purchase_price,
                "closing_costs": opportunity.acquisition.closing_costs,
                "rehab_cost": opportunity.acquisition.rehab_cost,
                "monthly_rent": opportunity.monthly_rent,
                "source": "extraction_pipeline",

                # Preserve source claims for reconciliation after underwriting.
                "source_purchase_price": source.claimed_purchase_price,
                "source_rent": source.claimed_rent,
                "source_cashflow": source.claimed_cashflow,
                "source_roi": source.claimed_roi,
                "source_cap_rate": source.claimed_cap_rate,
                "source_cash_on_cash": source.claimed_cash_on_cash_return,
                "source_document": source.source_document,
            }

        if isinstance(opportunity, AcquisitionOpportunity):
            return {
                "address": opportunity.address,
                "city": opportunity.city,
                "state": opportunity.state,
                "zip_code": opportunity.zip_code,
                "purchase_price": opportunity.purchase_price,
                "monthly_rent": opportunity.monthly_rent,
                "monthly_expenses": opportunity.monthly_expenses,
                "market": opportunity.market,
                "source": opportunity.source,
            }

        return {key: value for key, value in opportunity.fields.items()}
