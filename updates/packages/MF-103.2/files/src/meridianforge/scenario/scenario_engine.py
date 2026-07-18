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
