"""
Investor package service.

Creates complete investor deliverable packages.
"""

from pathlib import Path

from meridianforge.operations.report_archive import (
    ReportArchiveService,
)
from meridianforge.presentation.export_service import (
    InvestorReportExportService,
)
from meridianforge.product.weekly_review import WeeklyInvestorReview


class InvestorPackageService:
    """
    Generate and archive complete investor packages.
    """

    def __init__(self) -> None:

        self.export_service = InvestorReportExportService()
        self.archive_service = ReportArchiveService()

    def create_package(
        self,
        review: WeeklyInvestorReview,
        output_directory: Path,
        archive_root: Path,
    ) -> Path:
        """
        Generate reports and archive package.
        """

        files = self.export_service.export(
            review,
            output_directory,
        )

        metadata = {
            "report_count": len(files),
            "recommendations": [card.recommendation for card in review.cards],
            "confidence_scores": [card.confidence for card in review.cards],
        }

        return self.archive_service.archive(
            files,
            metadata,
            archive_root,
        )
