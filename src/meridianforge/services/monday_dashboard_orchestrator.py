from __future__ import annotations

from pathlib import Path

from meridianforge.product.weekly_review import WeeklyInvestorReview
from meridianforge.services.monday_artifact_service import MondayArtifactService


class MondayDashboardOrchestrator:
    """
    SP-490.3

    Canonical dashboard generation boundary.

    WeeklyInvestorReview
        ↓
    MondayArtifactService
        ↓
    Dashboard.txt / Dashboard.json / BUY / WATCH / PASS
    """

    def __init__(
        self,
        artifacts: MondayArtifactService | None = None,
    ) -> None:
        self.artifacts = artifacts or MondayArtifactService()

    def generate(
        self,
        review: WeeklyInvestorReview,
        output_directory: Path,
    ) -> Path:
        return self.artifacts.generate(
            review,
            output_directory,
        )
