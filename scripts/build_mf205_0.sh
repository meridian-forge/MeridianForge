#!/bin/bash

set -e

PACKAGE="updates/packages/MF-205.0"

echo "======================================"
echo "BUILD MF-205.0 RECOMMENDATION ENGINE FOUNDATION"
echo "======================================"

rm -rf "$PACKAGE"

mkdir -p \
"$PACKAGE/files/src/meridianforge/intelligence/profiles" \
"$PACKAGE/files/src/meridianforge/intelligence/recommendation" \
"$PACKAGE/files/tests/intelligence"


cat > "$PACKAGE/manifest.txt" <<'EOF'
MF-205.0

Investment Recommendation Engine Foundation

Adds:
- Investor profile model
- Recommendation engine foundation
- Decision rules framework
- Recommendation explanations
- Intelligence layer tests
EOF


cat > "$PACKAGE/release_notes.md" <<'EOF'
# MF-205.0

Investment Recommendation Engine Foundation

Meridian Forge now begins converting underwriting
results into investor-oriented recommendations.

Added:
- Investor preference modeling
- BUY / HOLD / PASS recommendation framework
- Rule-based recommendation foundation
- Human-readable explanations
EOF


cat > "$PACKAGE/files/src/meridianforge/intelligence/profiles/__init__.py" <<'EOF'
"""
Investor profile models.
"""
EOF


cat > "$PACKAGE/files/src/meridianforge/intelligence/profiles/investor.py" <<'EOF'
from dataclasses import dataclass


@dataclass
class InvestorProfile:
    """
    Defines investor decision preferences.
    """

    name: str
    goal: str
    risk_tolerance: str
    minimum_cash_flow: float = 0.0
    appreciation_priority: bool = False
EOF


cat > "$PACKAGE/files/src/meridianforge/intelligence/recommendation/__init__.py" <<'EOF'
"""
Recommendation engine components.
"""
EOF


cat > "$PACKAGE/files/src/meridianforge/intelligence/recommendation/rules.py" <<'EOF'
def evaluate_rules(
    cash_flow: float,
    dscr: float,
    appreciation_score: float,
) -> str:
    """
    Basic investment decision rules.
    """

    if (
        cash_flow > 0
        and dscr >= 1.20
        and appreciation_score >= 70
    ):
        return "BUY"

    if cash_flow > 0 and dscr >= 1.0:
        return "HOLD"

    return "PASS"
EOF


cat > "$PACKAGE/files/src/meridianforge/intelligence/recommendation/explanations.py" <<'EOF'
def generate_explanation(
    recommendation: str,
) -> list[str]:
    """
    Creates investor-readable reasoning.
    """

    explanations = {
        "BUY": [
            "Positive cash flow",
            "Healthy debt coverage",
            "Strong appreciation alignment",
        ],
        "HOLD": [
            "Acceptable fundamentals",
            "Additional review recommended",
        ],
        "PASS": [
            "Does not meet investment thresholds",
        ],
    }

    return explanations.get(
        recommendation,
        [],
    )
EOF


cat > "$PACKAGE/files/src/meridianforge/intelligence/recommendation/engine.py" <<'EOF'
from dataclasses import dataclass

from meridianforge.intelligence.recommendation.explanations import (
    generate_explanation,
)

from meridianforge.intelligence.recommendation.rules import (
    evaluate_rules,
)


@dataclass
class Recommendation:
    action: str
    reasons: list[str]


def recommend(
    cash_flow: float,
    dscr: float,
    appreciation_score: float,
) -> Recommendation:
    """
    Generate investment recommendation.
    """

    action = evaluate_rules(
        cash_flow,
        dscr,
        appreciation_score,
    )

    return Recommendation(
        action=action,
        reasons=generate_explanation(action),
    )
EOF


cat > "$PACKAGE/files/tests/intelligence/test_recommendation.py" <<'EOF'
from meridianforge.intelligence.recommendation.engine import (
    recommend,
)


def test_buy_recommendation() -> None:

    result = recommend(
        cash_flow=300,
        dscr=1.35,
        appreciation_score=80,
    )

    assert result.action == "BUY"


def test_pass_recommendation() -> None:

    result = recommend(
        cash_flow=-100,
        dscr=0.8,
        appreciation_score=40,
    )

    assert result.action == "PASS"
EOF


echo
echo "MF-205.0 PACKAGE CREATED"