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
from meridianforge.services.acquisition_orchestrator import (
    AcquisitionOrchestrator,
)
from meridianforge.services.acquisition_intake_service import (
    AcquisitionIntakeService,
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

        self.intake_service = (
            intake_service
            or AcquisitionIntakeService()
        )

        self.orchestrator = (
            orchestrator
            or AcquisitionOrchestrator()
        )

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

        acquisition_input = (
            self.intake_service.create_opportunity(
                opportunity,
            )
        )

        records = [
            acquisition_input.__dict__
            if hasattr(acquisition_input, "__dict__")
            else acquisition_input
        ]

        return self.orchestrator.analyze(
            records,
            investor_profile,
            export_path,
            archive_path,
        )
