"""
Acquisition execution service.

Bridges intake opportunities and acquisition opportunities
into the canonical acquisition orchestration pipeline.
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
        opportunity: IntakeOpportunity | AcquisitionOpportunity,
        investor_profile: InvestorProfile,
        export_path: Path | None = None,
        archive_path: Path | None = None,
    ) -> AcquisitionOrchestrationResult:
        """
        Execute acquisition analysis from either an intake opportunity
        or a canonical acquisition opportunity.
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
        opportunity: IntakeOpportunity | AcquisitionOpportunity,
    ) -> dict[str, object]:
        """
        Convert either opportunity model into the normalized record
        format expected by AcquisitionOrchestrator.
        """

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
