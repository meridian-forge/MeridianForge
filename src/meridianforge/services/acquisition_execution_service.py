"""
Acquisition execution service.

Bridges normalized opportunities
into complete acquisition intelligence workflow.
"""

from pathlib import Path

from meridianforge.models.domain.investor_profile import (
    InvestorProfile,
)
from meridianforge.models.results.acquisition_orchestration_result import (
    AcquisitionOrchestrationResult,
)
from meridianforge.opportunity.models import Opportunity
from meridianforge.services.acquisition_intake_service import (
    AcquisitionIntakeService,
)
from meridianforge.services.acquisition_orchestrator import (
    AcquisitionOrchestrator,
)


class AcquisitionExecutionService:
    """
    Executes complete acquisition workflow
    from normalized opportunity to investor output.
    """

    def __init__(
        self,
        intake_service: AcquisitionIntakeService | None = None,
        orchestrator: AcquisitionOrchestrator | None = None,
    ) -> None:

        self.intake_service = intake_service or AcquisitionIntakeService()
        self.orchestrator = orchestrator or AcquisitionOrchestrator()

    def execute(
        self,
        opportunity: Opportunity,
        investor_profile: InvestorProfile,
        export_path: Path | None = None,
        archive_path: Path | None = None,
    ) -> AcquisitionOrchestrationResult:
        """
        Execute complete acquisition workflow.
        """

        acquisition_input = self.intake_service.create_opportunity(
            opportunity.fields,
        )

        records = [
            {
                "address": acquisition_input.address,
                "city": acquisition_input.city,
                "state": acquisition_input.state,
                "zip_code": acquisition_input.zip_code,
                "purchase_price": acquisition_input.purchase_price,
                "monthly_rent": acquisition_input.monthly_rent,
                "monthly_expenses": acquisition_input.monthly_expenses,
                "market": acquisition_input.market,
                "source": acquisition_input.source,
            }
        ]

        return self.orchestrator.analyze(
            records,
            investor_profile,
            export_path,
            archive_path,
        )
