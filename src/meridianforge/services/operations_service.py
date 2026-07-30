from __future__ import annotations

from datetime import datetime
from pathlib import Path

from meridianforge.artifacts.artifact_lifecycle_service import (
    ArtifactLifecycleService,
)
from meridianforge.artifacts.artifact_status import (
    ArtifactStatus,
)
from meridianforge.models.domain.investment_strategy import (
    InvestmentStrategy,
)
from meridianforge.models.domain.investor_profile import (
    InvestorProfile,
)
from meridianforge.models.operations import (
    OperationsRunResult,
)
from meridianforge.product.weekly_review import (
    WeeklyInvestorReview,
)
from meridianforge.repositories.artifact_repository import (
    ArtifactRepository,
)
from meridianforge.services.folder_analysis_service import (
    FolderAnalysisService,
)
from meridianforge.services.monday_artifact_service import (
    MondayArtifactService,
)
from meridianforge.services.review_aggregator import (
    ReviewAggregator,
)


class OperationsService:
    """
    Coordinates MeridianForge Monday operations.
    """

    def __init__(
        self,
        deals_directory: Path,
    ) -> None:

        self.deals_directory = deals_directory

        self.output_directory = Path("runtime") / "outputs" / "monday"

        self.folder_analysis = FolderAnalysisService()

        self.artifact_service = MondayArtifactService()

        self.lifecycle = ArtifactLifecycleService()

        self.artifact_repository = ArtifactRepository()

    def discover_files(self) -> list[Path]:
        """
        Discover incoming opportunity artifacts.
        """

        if not self.deals_directory.exists():
            return []

        return sorted(
            [path for path in self.deals_directory.iterdir() if path.is_file()]
        )

    def execute(self) -> OperationsRunResult:
        """
        Execute Monday operational workflow.
        """

        started_at = datetime.now()

        result = OperationsRunResult(
            started_at=started_at,
        )

        discovered = self.discover_files()

        result.files_discovered.extend(discovered)

        if not discovered:
            result.completed_at = datetime.now()
            return result

        artifacts = []

        for path in discovered:

            artifact = self.artifact_repository.register(
                path,
                source="operations",
            )

            artifact = self.lifecycle.validate(
                artifact,
            )

            if artifact.status == ArtifactStatus.READY:
                artifacts.append(
                    artifact,
                )

            else:
                result.failed_files.append(
                    path,
                )

                if artifact.error:
                    result.errors.append(
                        f"{path.name}: {artifact.error}",
                    )

        if not artifacts:
            result.completed_at = datetime.now()
            return result

        investor = InvestorProfile(
            name="Default Investor",
            strategy=InvestmentStrategy.CASH_FLOW,
        )

        orchestration_results = self.folder_analysis.analyze_folder(
            self.deals_directory,
            investor_profile=investor,
        )

        valid_results = [
            item for item in orchestration_results if item.review is not None
        ]

        reviews = [item.review for item in valid_results if item.review is not None]

        portfolio_review = (
            ReviewAggregator.combine(reviews) if reviews else WeeklyInvestorReview()
        )

        dashboard_directory = self.artifact_service.generate(
            portfolio_review,
            self.output_directory,
        )

        for artifact in artifacts:

            self.lifecycle.mark_analyzed(
                artifact,
            )

            self.lifecycle.archive(
                artifact,
            )

        result.dashboard_path = dashboard_directory

        result.files_processed.extend(
            [artifact.path for artifact in artifacts],
        )

        result.analyses_completed = len(
            valid_results,
        )

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
