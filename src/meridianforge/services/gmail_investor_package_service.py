from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from meridianforge.models.domain.investor_profile import InvestorProfile
from meridianforge.services.gmail_production_acquisition_service import (
    GmailProductionAcquisitionResult,
    GmailProductionAcquisitionService,
)
from meridianforge.workflows.email_artifact_extraction_workflow import (
    EmailExtractionBatch,
)


@dataclass(frozen=True, slots=True)
class GmailInvestorPackageResult:
    analyzed_opportunities: int
    package_location: Path
    report: str


class GmailInvestorPackageService:
    """
    Generate a production investor package from Gmail-derived opportunities.

    MF-470.3
    """

    def __init__(
        self,
        acquisition: GmailProductionAcquisitionService | None = None,
    ) -> None:
        self._acquisition = acquisition or GmailProductionAcquisitionService()

    def execute(
        self,
        extraction_batch: EmailExtractionBatch,
        investor_profile: InvestorProfile,
        output_directory: Path,
    ) -> GmailInvestorPackageResult:
        acquisition_result: GmailProductionAcquisitionResult = (
            self._acquisition.execute(
                extraction_batch,
                investor_profile,
            )
        )

        output_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        package_path = output_directory / "gmail_investor_package.md"

        report = (
            "# MeridianForge Gmail Investor Package\n\n"
            f"Analyzed opportunities: {acquisition_result.analyzed_opportunities}\n"
        )

        package_path.write_text(
            report,
            encoding="utf-8",
        )

        return GmailInvestorPackageResult(
            analyzed_opportunities=acquisition_result.analyzed_opportunities,
            package_location=package_path,
            report=report,
        )
