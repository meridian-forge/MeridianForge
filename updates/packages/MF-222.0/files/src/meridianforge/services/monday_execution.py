from pathlib import Path
from typing import Any

from meridianforge.intake.property_import_service import (
    PropertyImportService,
)
from meridianforge.reporting.monday_dashboard import (
    MondayDashboardGenerator,
)
from meridianforge.reporting.portfolio_summary import (
    PortfolioSummary,
)


class MondayExecutionService:
    """
    Executes Monday analysis from imported properties.
    """

    def __init__(self) -> None:
        self.importer = PropertyImportService()
        self.summary = PortfolioSummary()
        self.dashboard = MondayDashboardGenerator()

    def execute(
        self,
        file_path: Path,
    ) -> str:

        opportunities: list[dict[str, Any]] = self.importer.import_csv(file_path)

        portfolio_summary = self.summary.summarize(opportunities)

        return self.dashboard.generate(portfolio_summary)
