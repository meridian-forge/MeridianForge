#!/bin/bash

set -e

echo "======================================"
echo "Meridian Forge MF-220.0"
echo "MVP Usable Analyzer Release"
echo "======================================"

mkdir -p \
src/meridianforge/workspace \
src/meridianforge/cli \
tests/cli \
updates/packages/MF-220.0/files/src/meridianforge/workspace \
updates/packages/MF-220.0/files/src/meridianforge/cli \
updates/packages/MF-220.0/files/tests/cli


cat > src/meridianforge/workspace/sample_opportunities.py <<'PY'
from typing import Any


def load_sample_opportunities() -> list[dict[str, Any]]:
    """
    Starter opportunity dataset.

    Later replaced by:
    - Zillow imports
    - realtor feeds
    - CSV uploads
    - API integrations
    """

    return [
        {
            "name": "Jacksonville Rental A",
            "status": "BUY",
            "score": 92,
        },
        {
            "name": "Philadelphia Rental B",
            "status": "WATCH",
            "score": 76,
        },
        {
            "name": "Memphis Rental C",
            "status": "BUY",
            "score": 88,
        },
    ]
PY


cat > src/meridianforge/cli/monday_command.py <<'PY'
from pathlib import Path

from meridianforge.reporting.monday_dashboard import (
    MondayDashboardGenerator,
)
from meridianforge.reporting.portfolio_summary import (
    PortfolioSummary,
)
from meridianforge.ranking.pipeline import (
    RankingPipeline,
)
from meridianforge.workspace.sample_opportunities import (
    load_sample_opportunities,
)


def run_monday() -> Path:
    """
    Executes the first usable Monday analyzer flow.
    """

    opportunities = (
        load_sample_opportunities()
    )

    ranked = RankingPipeline().rank(
        opportunities
    )

    summary = PortfolioSummary().summarize(
        ranked
    )

    dashboard = (
        MondayDashboardGenerator()
        .generate(summary)
    )

    output = Path(
        "MeridianForge_Monday_Dashboard.md"
    )

    output.write_text(
        dashboard,
        encoding="utf-8",
    )

    return output
PY


cat > tests/cli/test_monday_command.py <<'PY'
from meridianforge.cli.monday_command import (
    run_monday,
)


def test_monday_command_creates_dashboard(
    tmp_path,
    monkeypatch,
) -> None:

    monkeypatch.chdir(tmp_path)

    output = run_monday()

    assert output.exists()

    content = (
        output.read_text()
    )

    assert "Meridian Forge Monday Dashboard" in content
PY


cp src/meridianforge/workspace/sample_opportunities.py \
updates/packages/MF-220.0/files/src/meridianforge/workspace/


cp src/meridianforge/cli/monday_command.py \
updates/packages/MF-220.0/files/src/meridianforge/cli/


cp tests/cli/test_monday_command.py \
updates/packages/MF-220.0/files/tests/cli/


cat > updates/packages/MF-220.0/manifest.txt <<'TXT'
MF-220.0
MVP Usable Analyzer Release

Files:
src/meridianforge/workspace/sample_opportunities.py
src/meridianforge/cli/monday_command.py
tests/cli/test_monday_command.py
TXT


cat > updates/packages/MF-220.0/release_notes.md <<'MD'
# MF-220.0 MVP Usable Analyzer Release

First end-to-end usable workflow.

Capabilities:
- loads opportunities
- ranks opportunities
- creates portfolio summary
- generates Monday dashboard

Command path:
python -m meridianforge monday
MD


chmod +x scripts/build_mf220_0.sh

echo ""
echo "MF-220.0 build complete"
echo "Run ./scripts/quality_gate.sh"
