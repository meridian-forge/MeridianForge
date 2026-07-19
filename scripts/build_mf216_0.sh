#!/bin/bash

set -e

echo "======================================"
echo "Meridian Forge MF-216.0"
echo "Ranking Pipeline"
echo "======================================"

mkdir -p \
src/meridianforge/ranking \
tests/ranking \
updates/packages/MF-216.0/files/src/meridianforge/ranking \
updates/packages/MF-216.0/files/tests/ranking


cat > src/meridianforge/ranking/__init__.py <<'PY'
"""Meridian Forge ranking engine."""
PY


cat > src/meridianforge/ranking/pipeline.py <<'PY'
from typing import Any


class RankingPipeline:
    """
    Ranks analyzed opportunities.

    Initial ranking uses a configurable score field.
    """

    def __init__(
        self,
        score_key: str = "score",
    ) -> None:
        self.score_key = score_key

    def rank(
        self,
        opportunities: list[Any],
    ) -> list[Any]:

        return sorted(
            opportunities,
            key=lambda item: self._score(item),
            reverse=True,
        )

    def _score(
        self,
        opportunity: Any,
    ) -> float:

        if isinstance(opportunity, dict):
            return float(
                opportunity.get(
                    self.score_key,
                    0,
                )
            )

        return 0.0
PY


cat > tests/ranking/test_pipeline.py <<'PY'
from meridianforge.ranking.pipeline import (
    RankingPipeline,
)


def test_ranking_orders_highest_score_first() -> None:

    pipeline = RankingPipeline()

    opportunities = [
        {
            "name": "Property A",
            "score": 70,
        },
        {
            "name": "Property B",
            "score": 90,
        },
        {
            "name": "Property C",
            "score": 80,
        },
    ]

    ranked = pipeline.rank(
        opportunities
    )

    assert ranked[0]["name"] == "Property B"
    assert ranked[1]["name"] == "Property C"
    assert ranked[2]["name"] == "Property A"
PY


cp src/meridianforge/ranking/pipeline.py \
updates/packages/MF-216.0/files/src/meridianforge/ranking/


cp tests/ranking/test_pipeline.py \
updates/packages/MF-216.0/files/tests/ranking/


cat > updates/packages/MF-216.0/manifest.txt <<'TXT'
MF-216.0
Ranking Pipeline

Files:
src/meridianforge/ranking/__init__.py
src/meridianforge/ranking/pipeline.py
tests/ranking/test_pipeline.py
TXT


cat > updates/packages/MF-216.0/release_notes.md <<'MD'
# MF-216.0 Ranking Pipeline

Adds opportunity prioritization.

Capabilities:
- rank analyzed opportunities
- sort by investment score
- prepare Monday priority output
MD


chmod +x scripts/build_mf216_0.sh

echo ""
echo "MF-216.0 build complete"
echo "Run ./scripts/quality_gate.sh"
