#!/bin/bash

set -e

PACKAGE="updates/packages/MF-104.0"

echo "======================================"
echo "BUILD MF-104.0 ACQUISITION INTELLIGENCE"
echo "======================================"

rm -rf "$PACKAGE"

mkdir -p \
"$PACKAGE/files/src/meridianforge/acquisition" \
"$PACKAGE/files/tests/acquisition"


cat > "$PACKAGE/manifest.txt" <<'EOF'
MF-104.0
Property Acquisition Intelligence

Adds:
- Acquisition scoring
- Decision engine
- Ranking foundation
EOF


cat > "$PACKAGE/release_notes.md" <<'EOF'
# MF-104.0 Property Acquisition Intelligence

Transforms underwriting results into acquisition decisions.

Outputs:
- BUY
- WATCH
- REJECT
EOF


cat > "$PACKAGE/files/src/meridianforge/acquisition/__init__.py" <<'PY'
PY


cat > "$PACKAGE/files/src/meridianforge/acquisition/criteria.py" <<'PY'
from dataclasses import dataclass


@dataclass
class AcquisitionCriteria:

    minimum_dscr: float = 1.20
    minimum_cap_rate: float = 0.05
    minimum_cash_return: float = 0.08
PY


cat > "$PACKAGE/files/src/meridianforge/acquisition/score.py" <<'PY'
from meridianforge.analysis.result import AnalysisResult
from meridianforge.acquisition.criteria import (
    AcquisitionCriteria,
)


def calculate_score(
    result: AnalysisResult,
    criteria: AcquisitionCriteria,
) -> float:

    score = 0.0

    if result.dscr >= criteria.minimum_dscr:
        score += 35

    if result.cap_rate >= criteria.minimum_cap_rate:
        score += 35

    if (
        result.cash_on_cash_return
        >= criteria.minimum_cash_return
    ):
        score += 30

    return score
PY


cat > "$PACKAGE/files/src/meridianforge/acquisition/decision.py" <<'PY'
from dataclasses import dataclass


@dataclass
class AcquisitionDecision:

    status: str
    score: float
    reasons: list[str]
PY


cat > "$PACKAGE/files/src/meridianforge/acquisition/ranking.py" <<'PY'
from meridianforge.acquisition.decision import (
    AcquisitionDecision,
)


def rank(
    decisions: list[AcquisitionDecision],
) -> list[AcquisitionDecision]:

    return sorted(
        decisions,
        key=lambda item: item.score,
        reverse=True,
    )
PY


cat > "$PACKAGE/files/tests/acquisition/test_score.py" <<'PY'
from meridianforge.acquisition.criteria import (
    AcquisitionCriteria,
)
from meridianforge.acquisition.score import (
    calculate_score,
)
from meridianforge.analysis.result import (
    AnalysisResult,
)


def test_score():

    result = AnalysisResult(
        cash_flow_monthly=300,
        cap_rate=0.06,
        cash_on_cash_return=0.10,
        dscr=1.5,
        score=0,
    )

    score = calculate_score(
        result,
        AcquisitionCriteria(),
    )

    assert score == 100
PY


cat > "$PACKAGE/files/tests/acquisition/test_ranking.py" <<'PY'
from meridianforge.acquisition.decision import (
    AcquisitionDecision,
)
from meridianforge.acquisition.ranking import (
    rank,
)


def test_ranking():

    result = rank(
        [
            AcquisitionDecision(
                "WATCH",
                50,
                [],
            ),
            AcquisitionDecision(
                "BUY",
                90,
                [],
            ),
        ]
    )

    assert result[0].status == "BUY"
PY


echo
echo "MF-104.0 PACKAGE CREATED"