#!/bin/bash

set -e

PACKAGE="updates/packages/MF-202.1"

echo "======================================"
echo "BUILD MF-202.1 RANKING ENGINE"
echo "======================================"

rm -rf "$PACKAGE"

mkdir -p \
"$PACKAGE/files/src/meridianforge/ranking" \
"$PACKAGE/files/tests/ranking"


cat > "$PACKAGE/manifest.txt" <<'EOF'
MF-202.1

Ranking Engine

Adds:
- Opportunity scoring
- Ranking model
- Recommendation priority
- Ranking tests
EOF


cat > "$PACKAGE/release_notes.md" <<'EOF'
# MF-202.1

Adds the first transparent opportunity ranking engine.

Purpose:

Prioritize investment opportunities using capital allocation principles.
EOF


cat > "$PACKAGE/files/src/meridianforge/ranking/models.py" <<'EOF'
from dataclasses import dataclass


@dataclass
class RankingResult:

    opportunity_file: str

    score: float

    rank: int = 0
EOF


cat > "$PACKAGE/files/src/meridianforge/ranking/engine.py" <<'EOF'
from meridianforge.analysis.models import AnalysisResult
from meridianforge.ranking.models import RankingResult


def calculate_score(
    analysis: AnalysisResult,
) -> float:

    score = 50.0


    if "cash_on_cash" in analysis.metrics:

        coc = analysis.metrics["cash_on_cash"]

        score += min(
            coc * 100,
            20,
        )


    if "dscr" in analysis.metrics:

        dscr = analysis.metrics["dscr"]

        if dscr >= 1.25:
            score += 15


    if analysis.warnings:

        score -= (
            len(analysis.warnings)
            * 5
        )


    return max(
        0,
        min(
            score,
            100,
        ),
    )


def rank(
    analyses: list[AnalysisResult],
) -> list[RankingResult]:

    ranked = [

        RankingResult(
            opportunity_file=result.opportunity_file,
            score=calculate_score(result),
        )

        for result in analyses
    ]


    ranked.sort(
        key=lambda item: item.score,
        reverse=True,
    )


    for index, item in enumerate(
        ranked,
        start=1,
    ):

        item.rank = index


    return ranked
EOF


cat > "$PACKAGE/files/tests/ranking/test_engine.py" <<'EOF'
from meridianforge.analysis.models import AnalysisResult
from meridianforge.ranking.engine import calculate_score


def test_score_calculation() -> None:

    result = AnalysisResult(
        opportunity_file="property.xlsx",
        metrics={
            "cash_on_cash": 0.12,
            "dscr": 1.35,
        },
    )


    score = calculate_score(result)


    assert score > 60
EOF


echo
echo "MF-202.1 PACKAGE CREATED"