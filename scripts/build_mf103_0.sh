#!/bin/bash

set -e

PACKAGE="updates/packages/MF-103.0"

echo "======================================"
echo "BUILD MF-103.0 UNDERWRITING PIPELINE"
echo "======================================"

rm -rf "$PACKAGE"

mkdir -p \
"$PACKAGE/files/src/meridianforge/analysis" \
"$PACKAGE/files/tests/analysis"


cat > "$PACKAGE/manifest.txt" <<'EOF'
MF-103.0
Underwriting Pipeline Integration

Adds:
- Analysis Result model
- Investment metrics
- Underwriting engine
- Analyzer workflow
EOF


cat > "$PACKAGE/release_notes.md" <<'EOF'
# MF-103.0 Underwriting Pipeline

Connects opportunities to financial analysis.

Adds:
- Cash flow metrics
- Cap rate
- Cash-on-cash return
- DSCR foundation
- Investment scoring
EOF


cat > "$PACKAGE/files/src/meridianforge/analysis/result.py" <<'PY'
from dataclasses import dataclass


@dataclass
class AnalysisResult:
    cash_flow_monthly: float
    cap_rate: float
    cash_on_cash_return: float
    dscr: float
    score: float
PY


cat > "$PACKAGE/files/src/meridianforge/analysis/metrics.py" <<'PY'
def calculate_cap_rate(
    annual_noi: float,
    purchase_price: float,
) -> float:

    if purchase_price <= 0:
        raise ValueError(
            "Purchase price must be positive"
        )

    return annual_noi / purchase_price



def calculate_cash_on_cash(
    annual_cash_flow: float,
    cash_invested: float,
) -> float:

    if cash_invested <= 0:
        raise ValueError(
            "Cash invested must be positive"
        )

    return annual_cash_flow / cash_invested



def calculate_dscr(
    noi: float,
    annual_debt: float,
) -> float:

    if annual_debt <= 0:
        raise ValueError(
            "Debt service must be positive"
        )

    return noi / annual_debt
PY


cat > "$PACKAGE/files/src/meridianforge/analysis/underwriting_engine.py" <<'PY'
from meridianforge.analysis.metrics import (
    calculate_cap_rate,
    calculate_cash_on_cash,
    calculate_dscr,
)

from meridianforge.analysis.result import AnalysisResult


class UnderwritingEngine:

    def analyze(
        self,
        purchase_price: float,
        noi: float,
        annual_cash_flow: float,
        cash_invested: float,
        annual_debt: float,
    ) -> AnalysisResult:

        cap_rate = calculate_cap_rate(
            noi,
            purchase_price,
        )

        cash_return = calculate_cash_on_cash(
            annual_cash_flow,
            cash_invested,
        )

        dscr = calculate_dscr(
            noi,
            annual_debt,
        )

        score = (
            cap_rate
            + cash_return
            + dscr
        )

        return AnalysisResult(
            cash_flow_monthly=annual_cash_flow / 12,
            cap_rate=cap_rate,
            cash_on_cash_return=cash_return,
            dscr=dscr,
            score=score,
        )
PY


cat > "$PACKAGE/files/src/meridianforge/analysis/analyzer.py" <<'PY'
from meridianforge.analysis.underwriting_engine import (
    UnderwritingEngine,
)


class Analyzer:

    def __init__(self) -> None:
        self.engine = UnderwritingEngine()

    def run(self, **kwargs):
        return self.engine.analyze(**kwargs)
PY


cat > "$PACKAGE/files/src/meridianforge/analysis/__init__.py" <<'PY'
PY


cat > "$PACKAGE/files/tests/analysis/test_metrics.py" <<'PY'
from meridianforge.analysis.metrics import (
    calculate_cap_rate,
    calculate_dscr,
)


def test_cap_rate():

    assert calculate_cap_rate(
        12000,
        200000,
    ) == 0.06



def test_dscr():

    assert calculate_dscr(
        24000,
        12000,
    ) == 2
PY


cat > "$PACKAGE/files/tests/analysis/test_engine.py" <<'PY'
from meridianforge.analysis.underwriting_engine import (
    UnderwritingEngine,
)


def test_engine():

    result = UnderwritingEngine().analyze(
        purchase_price=200000,
        noi=12000,
        annual_cash_flow=6000,
        cash_invested=50000,
        annual_debt=8000,
    )

    assert result.cap_rate == 0.06
    assert result.dscr == 1.5
PY


echo
echo "MF-103.0 PACKAGE CREATED"