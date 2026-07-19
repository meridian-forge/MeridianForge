from pathlib import Path

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


def run_monday() -> Path:
    """
    Executes the first usable Monday analyzer flow.
    """

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
