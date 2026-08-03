from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from meridianforge.models.domain.investor_profile import InvestorProfile
from meridianforge.services.gmail_investor_package_service import (
    GmailInvestorPackageResult,
    GmailInvestorPackageService,
)
from meridianforge.workflows.email_artifact_extraction_workflow import (
    EmailExtractionBatch,
)


@dataclass(frozen=True, slots=True)
class MondayGmailExecutionResult:
    analyzed_opportunities: int
    package_location: Path
    dashboard: str


class MondayGmailExecutionService:
    """
    Execute the production Monday Gmail workflow.

    MF-470.4
    """

    def __init__(
        self,
        package_service: GmailInvestorPackageService | None = None,
    ) -> None:
        self._package_service = package_service or GmailInvestorPackageService()

    def execute(
        self,
        extraction_batch: EmailExtractionBatch,
        investor_profile: InvestorProfile,
        output_directory: Path,
    ) -> MondayGmailExecutionResult:
        package: GmailInvestorPackageResult = self._package_service.execute(
            extraction_batch,
            investor_profile,
            output_directory,
        )

        dashboard = (
            "# MeridianForge Monday Gmail Execution\n\n"
            f"Analyzed opportunities: {package.analyzed_opportunities}\n"
            f"Package: {package.package_location}\n"
        )

        return MondayGmailExecutionResult(
            analyzed_opportunities=package.analyzed_opportunities,
            package_location=package.package_location,
            dashboard=dashboard,
        )
