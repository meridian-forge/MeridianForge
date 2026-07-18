#!/bin/bash

set -e

PACKAGE="updates/packages/MF-202.0"

echo "======================================"
echo "BUILD MF-202.0 ANALYSIS FOUNDATION"
echo "======================================"

rm -rf "$PACKAGE"

mkdir -p \
"$PACKAGE/files/src/meridianforge/analysis" \
"$PACKAGE/files/tests/analysis"


cat > "$PACKAGE/manifest.txt" <<'EOF'
MF-202.0

Analysis Result Foundation

Adds:
- Analysis models
- Return metrics
- Analyzer framework
- Tests
EOF


cat > "$PACKAGE/files/src/meridianforge/analysis/models.py" <<'EOF'
from dataclasses import dataclass, field
from enum import StrEnum


class Recommendation(StrEnum):
    BUY = "BUY"
    WATCH = "WATCH"
    REJECT = "REJECT"


@dataclass
class AnalysisResult:
    opportunity_file: str
    metrics: dict[str, float] = field(default_factory=dict)
    recommendation: Recommendation = Recommendation.WATCH
    warnings: list[str] = field(default_factory=list)
EOF


cat > "$PACKAGE/files/src/meridianforge/analysis/metrics.py" <<'EOF'
def calculate_cash_on_cash(
    annual_cash_flow: float,
    cash_invested: float,
) -> float:

    if cash_invested == 0:
        return 0.0

    return annual_cash_flow / cash_invested


def cash_on_cash_return(
    annual_cash_flow: float,
    cash_invested: float,
) -> float:

    return calculate_cash_on_cash(
        annual_cash_flow,
        cash_invested,
    )


def roi(
    profit: float,
    investment: float,
) -> float:

    if investment == 0:
        return 0.0

    return profit / investment


def calculate_cap_rate(
    annual_noi: float,
    property_value: float,
) -> float:

    if property_value == 0:
        return 0.0

    return annual_noi / property_value


def calculate_dscr(
    annual_noi: float,
    annual_debt_service: float,
) -> float:

    if annual_debt_service == 0:
        return 0.0

    return annual_noi / annual_debt_service
EOF


cat > "$PACKAGE/files/src/meridianforge/analysis/analyzer.py" <<'EOF'
from meridianforge.analysis.models import (
    AnalysisResult,
    Recommendation,
)
from meridianforge.opportunity.models import Opportunity


def analyze(
    opportunity: Opportunity,
) -> AnalysisResult:

    warnings: list[str] = []

    if not opportunity.fields:
        warnings.append(
            "Missing financial data"
        )

    return AnalysisResult(
        opportunity_file=opportunity.source_file,
        recommendation=Recommendation.WATCH,
        warnings=warnings,
    )
EOF


cat > "$PACKAGE/files/tests/analysis/test_metrics.py" <<'EOF'
from meridianforge.analysis.metrics import (
    cash_on_cash_return,
    roi,
)


def test_cash_on_cash_return() -> None:
    assert cash_on_cash_return(
        4000,
        30000,
    ) == 4000 / 30000


def test_roi() -> None:
    assert roi(
        60000,
        200000,
    ) == 0.30
EOF


echo
echo "MF-202.0 PACKAGE CREATED"