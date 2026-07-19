#!/bin/bash

set -e

echo "======================================"
echo "Meridian Forge MF-217.0"
echo "Portfolio Summary Engine"
echo "======================================"

mkdir -p \
src/meridianforge/reporting \
tests/reporting \
updates/packages/MF-217.0/files/src/meridianforge/reporting \
updates/packages/MF-217.0/files/tests/reporting


cat > src/meridianforge/reporting/portfolio_summary.py <<'PY'
from typing import Any


class PortfolioSummary:
    """
    Builds executive summary statistics
    from analyzed opportunities.
    """

    def summarize(
        self,
        opportunities: list[Any],
    ) -> dict[str, Any]:

        total = len(opportunities)

        buy_count = sum(
            1
            for item in opportunities
            if self._status(item) == "BUY"
        )

        watch_count = sum(
            1
            for item in opportunities
            if self._status(item) == "WATCH"
        )

        scores = [
            self._score(item)
            for item in opportunities
        ]

        average_score = (
            sum(scores) / len(scores)
            if scores
            else 0
        )

        top_opportunity = (
            opportunities[0]
            if opportunities
            else None
        )

        return {
            "total_opportunities": total,
            "buy_count": buy_count,
            "watch_count": watch_count,
            "average_score": average_score,
            "top_opportunity": top_opportunity,
        }

    def _status(
        self,
        item: Any,
    ) -> str:

        if isinstance(item, dict):
            return str(
                item.get(
                    "status",
                    "",
                )
            )

        return ""

    def _score(
        self,
        item: Any,
    ) -> float:

        if isinstance(item, dict):
            return float(
                item.get(
                    "score",
                    0,
                )
            )

        return 0.0
PY


cat > tests/reporting/test_portfolio_summary.py <<'PY'
from meridianforge.reporting.portfolio_summary import (
    PortfolioSummary,
)


def test_portfolio_summary() -> None:

    summary = PortfolioSummary().summarize(
        [
            {
                "name": "A",
                "status": "BUY",
                "score": 90,
            },
            {
                "name": "B",
                "status": "WATCH",
                "score": 70,
            },
        ]
    )

    assert summary["total_opportunities"] == 2
    assert summary["buy_count"] == 1
    assert summary["watch_count"] == 1
    assert summary["average_score"] == 80
PY


cp src/meridianforge/reporting/portfolio_summary.py \
updates/packages/MF-217.0/files/src/meridianforge/reporting/


cp tests/reporting/test_portfolio_summary.py \
updates/packages/MF-217.0/files/tests/reporting/


cat > updates/packages/MF-217.0/manifest.txt <<'TXT'
MF-217.0
Portfolio Summary Engine

Files:
src/meridianforge/reporting/portfolio_summary.py
tests/reporting/test_portfolio_summary.py
TXT


cat > updates/packages/MF-217.0/release_notes.md <<'MD'
# MF-217.0 Portfolio Summary Engine

Adds executive summary generation.

Capabilities:
- opportunity counts
- BUY/WATCH statistics
- average scoring
- top opportunity identification
MD


chmod +x scripts/build_mf217_0.sh

echo ""
echo "MF-217.0 build complete"
echo "Run ./scripts/quality_gate.sh"
