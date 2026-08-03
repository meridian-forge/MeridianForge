from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from meridianforge.models.domain.investor_profile import InvestorProfile
from meridianforge.services.gmail_production_acquisition_service import (
    GmailProductionAcquisitionService,
)
from meridianforge.workflows.email_artifact_extraction_workflow import (
    EmailExtractionBatch,
)


@dataclass(frozen=True, slots=True)
class GmailProductionPackageResult:
    analyzed_opportunities: int
    package_location: Path


class GmailProductionPackageService:
    """
    Generate the production investor package from Gmail-derived opportunities.

    SP-480.3
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
    ) -> GmailProductionPackageResult:
        acquisition_result = self._acquisition.execute(
            extraction_batch,
            investor_profile,
        )

        output_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        package_path = output_directory / "investor_package.md"

        package_path.write_text(
            (
                "# MeridianForge Investor Package\n\n"
                f"Analyzed opportunities: "
                f"{acquisition_result.analyzed_opportunities}\n"
            ),
            encoding="utf-8",
        )

        return GmailProductionPackageResult(
            analyzed_opportunities=acquisition_result.analyzed_opportunities,
            package_location=package_path,
        )
