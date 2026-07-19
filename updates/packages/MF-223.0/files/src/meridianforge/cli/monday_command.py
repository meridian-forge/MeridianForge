from pathlib import Path
from typing import Any

from meridianforge.intake.property_import_service import (
    PropertyImportService,
)
from meridianforge.ranking.pipeline import (
    RankingPipeline,
)
from meridianforge.reporting.monday_dashboard import (
    MondayDashboardGenerator,
)
from meridianforge.reporting.portfolio_summary import (
    PortfolioSummary,
)
from meridianforge.workspace.sample_opportunities import (
    load_sample_opportunities,
)


def run_monday(
    file_path: Path | None = None,
) -> Path:
    """
    Executes the Monday analyzer flow.

    Uses CSV input when provided.
    Falls back to sample opportunities.
    """

    opportunities: list[dict[str, Any]]

    if file_path:
        opportunities = PropertyImportService().import_csv(file_path)
    else:
        opportunities = load_sample_opportunities()

    ranked = RankingPipeline().rank(opportunities)

    summary = PortfolioSummary().summarize(ranked)

    dashboard = MondayDashboardGenerator().generate(summary)

    output_dir = Path("runtime/outputs")

    output_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    output = output_dir / "MeridianForge_Monday_Dashboard.md"

    output.write_text(
        dashboard,
        encoding="utf-8",
    )

    return output
