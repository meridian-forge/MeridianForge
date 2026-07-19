#!/bin/bash

set -e

echo "======================================"
echo "Meridian Forge MF-218.0"
echo "Monday Dashboard Generator"
echo "======================================"

mkdir -p \
src/meridianforge/reporting \
tests/reporting \
updates/packages/MF-218.0/files/src/meridianforge/reporting \
updates/packages/MF-218.0/files/tests/reporting


cat > src/meridianforge/reporting/monday_dashboard.py <<'PY'
from typing import Any


class MondayDashboardGenerator:
    """
    Generates the executive Monday dashboard
    from portfolio summary data.
    """

    def generate(
        self,
        summary: dict[str, Any],
    ) -> str:

        top = summary.get(
            "top_opportunity",
            None,
        )

        top_name = (
            top.get("name", "N/A")
            if isinstance(top, dict)
            else "N/A"
        )

        top_score = (
            top.get("score", 0)
            if isinstance(top, dict)
            else 0
        )

        return (
            "Meridian Forge Monday Dashboard\n"
            "================================\n\n"
            f"Opportunities Reviewed: "
            f"{summary.get('total_opportunities', 0)}\n"
            f"BUY Candidates: "
            f"{summary.get('buy_count', 0)}\n"
            f"WATCH Candidates: "
            f"{summary.get('watch_count', 0)}\n"
            f"Average Score: "
            f"{summary.get('average_score', 0)}\n\n"
            "Top Opportunity:\n"
            f"- {top_name}\n"
            f"- Score: {top_score}\n"
        )
PY


cat > tests/reporting/test_monday_dashboard.py <<'PY'
from meridianforge.reporting.monday_dashboard import (
    MondayDashboardGenerator,
)


def test_dashboard_generation() -> None:

    dashboard = (
        MondayDashboardGenerator()
        .generate(
            {
                "total_opportunities": 5,
                "buy_count": 2,
                "watch_count": 3,
                "average_score": 82,
                "top_opportunity": {
                    "name": "Property A",
                    "score": 95,
                },
            }
        )
    )

    assert "Property A" in dashboard
    assert "BUY Candidates: 2" in dashboard
PY


cp src/meridianforge/reporting/monday_dashboard.py \
updates/packages/MF-218.0/files/src/meridianforge/reporting/


cp tests/reporting/test_monday_dashboard.py \
updates/packages/MF-218.0/files/tests/reporting/


cat > updates/packages/MF-218.0/manifest.txt <<'TXT'
MF-218.0
Monday Dashboard Generator

Files:
src/meridianforge/reporting/monday_dashboard.py
tests/reporting/test_monday_dashboard.py
TXT


cat > updates/packages/MF-218.0/release_notes.md <<'MD'
# MF-218.0 Monday Dashboard Generator

Adds executive dashboard output.

Capabilities:
- summarizes portfolio activity
- highlights BUY/WATCH candidates
- identifies top opportunity
- prepares Monday investor review
MD


chmod +x scripts/build_mf218_0.sh

echo ""
echo "MF-218.0 build complete"
echo "Run ./scripts/quality_gate.sh"
