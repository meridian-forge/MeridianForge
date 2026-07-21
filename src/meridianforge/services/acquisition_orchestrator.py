"""
Acquisition orchestration service.

Coordinates pipeline analysis,
decision intelligence,
and investor packaging.
"""

from pathlib import Path

from meridianforge.models.domain.investor_profile import (
    InvestorProfile,
)
from meridianforge.models.results.acquisition_orchestration_result import (
    AcquisitionOrchestrationResult,
)
from meridianforge.operations.investor_package_service import (
    InvestorPackageService,
)
from meridianforge.services.acquisition_intelligence import (
    AcquisitionIntelligenceService,
)
from meridianforge.services.investment_pipeline import (
    InvestmentPipeline,
)


class AcquisitionOrchestrator:
    """
    End-to-end acquisition intelligence coordinator.
    """

    def __init__(
        self,
        pipeline: InvestmentPipeline | None = None,
        intelligence: AcquisitionIntelligenceService | None = None,
        package_service: InvestorPackageService | None = None,
    ) -> None:

        self.pipeline = pipeline or InvestmentPipeline()

        self.intelligence = intelligence or AcquisitionIntelligenceService()

        self.package_service = package_service or InvestorPackageService()

    def analyze(
        self,
        records: list[dict[str, object]],
        investor_profile: InvestorProfile,
        export_path: Path | None = None,
        archive_path: Path | None = None,
    ) -> AcquisitionOrchestrationResult:
        """
        Execute complete acquisition analysis.
        """

        pipeline_result = self.pipeline.analyze(
            records,
            investor_profile,
        )

        review = self.intelligence.create_review(
            pipeline_result,
        )

        package_location = None

        if export_path and archive_path:
            package_location = self.package_service.create_package(
                review,
                export_path,
                archive_path,
            )

        return AcquisitionOrchestrationResult(
            review=review,
            package_location=package_location,
        )
