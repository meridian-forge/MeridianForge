"""
Operations orchestration service.

Coordinates the complete Monday operational workflow.

Responsibilities:
- discover incoming deal artifacts
- execute folder analysis
- aggregate investor reviews
- generate Monday artifacts
- return execution summary
"""

from __future__ import annotations

from datetime import datetime
from pathlib import Path

from meridianforge.models.domain.investment_strategy import InvestmentStrategy
from meridianforge.models.domain.investor_profile import InvestorProfile
from meridianforge.models.operations import OperationsRunResult
from meridianforge.product.weekly_review import WeeklyInvestorReview
from meridianforge.services.folder_analysis_service import FolderAnalysisService
from meridianforge.services.monday_artifact_service import MondayArtifactService
from meridianforge.services.review_aggregator import ReviewAggregator


class OperationsService:
    """
    Coordinates the complete MeridianForge Monday workflow.
    """

    def __init__(
        self,
        deals_directory: Path,
        output_directory: Path | None = None,
        folder_analysis: FolderAnalysisService | None = None,
        artifact_service: MondayArtifactService | None = None,
    ) -> None:
        self.deals_directory = deals_directory
        self.output_directory = output_directory or Path("runtime/outputs")
        self.folder_analysis = folder_analysis or FolderAnalysisService()
        self.artifact_service = artifact_service or MondayArtifactService()

    def discover_files(self) -> list[Path]:
        """
        Discover incoming investment artifacts.
        """

        if not self.deals_directory.exists():
            return []

        return sorted(path for path in self.deals_directory.iterdir() if path.is_file())

    def execute(self) -> OperationsRunResult:
        """
        Execute the Monday workflow.
        """

        started_at = datetime.now()

        result = OperationsRunResult(
            started_at=started_at,
        )

        discovered = self.discover_files()

        result.files_discovered.extend(
            discovered,
        )

        if not discovered:
            result.completed_at = datetime.now()
            return result

        investor = InvestorProfile(
            name="Default Investor",
            strategy=InvestmentStrategy.CASH_FLOW,
        )

        valid_results = []

        for file_path in discovered:
            try:
                single_result = self.folder_analysis.analyze_folder(
                    file_path.parent,
                    investor_profile=investor,
                )

                matching_results = [item for item in single_result if item]

                valid_results.extend(
                    matching_results,
                )

                if matching_results:
                    result.files_processed.append(
                        file_path,
                    )

            except Exception as exc:
                result.failed_files.append(
                    file_path,
                )

                result.errors.append(
                    f"{file_path.name}: {exc}",
                )

        reviews = [analysis.review for analysis in valid_results]

        portfolio_review = (
            ReviewAggregator.combine(reviews) if reviews else WeeklyInvestorReview()
        )

        if portfolio_review.cards:
            dashboard_dir = self.artifact_service.generate(
                portfolio_review,
                self.output_directory,
            )

            result.dashboard_path = dashboard_dir

        result.analyses_completed = len(valid_results)

        result.buy_count = len(
            portfolio_review.buy_candidates(),
        )

        result.watch_count = len(
            portfolio_review.watch_candidates(),
        )

        result.pass_count = len(
            [
                card
                for card in portfolio_review.cards
                if card.recommendation.upper() == "PASS"
            ],
        )

        result.completed_at = datetime.now()

        return result
