#!/bin/bash

set -e

PACKAGE="updates/packages/MF-103.2"

echo "======================================"
echo "BUILD MF-103.2 SCENARIO ENGINE"
echo "======================================"

rm -rf "$PACKAGE"

mkdir -p \
"$PACKAGE/files/src/meridianforge/scenario" \
"$PACKAGE/files/tests/scenario"


cat > "$PACKAGE/manifest.txt" <<'EOF'
MF-103.2
Scenario Engine

Adds:
- Scenario model
- Scenario execution engine
- Scenario comparison
EOF


cat > "$PACKAGE/release_notes.md" <<'EOF'
# MF-103.2 Scenario Engine

Adds multi-case underwriting.

Supports:
- Base case
- Conservative case
- Aggressive case
- Scenario comparison
EOF


cat > "$PACKAGE/files/src/meridianforge/scenario/__init__.py" <<'PY'
PY


cat > "$PACKAGE/files/src/meridianforge/scenario/scenario.py" <<'PY'
from dataclasses import dataclass


@dataclass
class Scenario:

    name: str

    rent_multiplier: float = 1.0
    vacancy_multiplier: float = 1.0
    expense_multiplier: float = 1.0
    interest_rate_multiplier: float = 1.0
PY


cat > "$PACKAGE/files/src/meridianforge/scenario/scenario_engine.py" <<'PY'
from meridianforge.finance.cashflow import (
    monthly_cash_flow,
)


class ScenarioEngine:

    def evaluate(
        self,
        scenario,
        rent: float,
        expenses: float,
        mortgage: float,
    ) -> float:

        adjusted_rent = (
            rent
            * scenario.rent_multiplier
        )

        adjusted_expenses = (
            expenses
            * scenario.expense_multiplier
        )

        return monthly_cash_flow(
            adjusted_rent,
            adjusted_expenses,
            mortgage,
        )
PY


cat > "$PACKAGE/files/src/meridianforge/scenario/comparison.py" <<'PY'
class ScenarioComparison:

    def compare(
        self,
        results: dict[str, float],
    ) -> dict[str, float]:

        return dict(
            sorted(
                results.items(),
                key=lambda item: item[1],
                reverse=True,
            )
        )
PY


cat > "$PACKAGE/files/tests/scenario/test_scenario_engine.py" <<'PY'
from meridianforge.scenario.scenario import Scenario
from meridianforge.scenario.scenario_engine import (
    ScenarioEngine,
)


def test_scenario():

    result = ScenarioEngine().evaluate(
        Scenario(
            "Base",
            rent_multiplier=1.1,
        ),
        2000,
        400,
        900,
    )

    assert result == 900
PY


cat > "$PACKAGE/files/tests/scenario/test_comparison.py" <<'PY'
from meridianforge.scenario.comparison import (
    ScenarioComparison,
)


def test_compare():

    result = ScenarioComparison().compare(
        {
            "bad": 100,
            "good": 300,
        }
    )

    assert list(result.keys())[0] == "good"
PY


echo
echo "MF-103.2 PACKAGE CREATED"