#!/bin/bash

set -e

FILE="updates/packages/MF-103.2/files/src/meridianforge/scenario/scenario_engine.py"

echo "======================================"
echo "MF-103.2 PACKAGE MYPY FIX"
echo "======================================"

cat > "$FILE" <<'PY'
from meridianforge.finance.cashflow import (
    monthly_cash_flow,
)

from meridianforge.scenario.scenario import Scenario


class ScenarioEngine:

    def evaluate(
        self,
        scenario: Scenario,
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

echo "MF-103.2 PACKAGE MYPY FIX COMPLETE"