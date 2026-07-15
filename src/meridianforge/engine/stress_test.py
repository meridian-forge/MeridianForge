"""
Stress testing engine.

Applies scenarios and evaluates
investment resilience.
"""

from dataclasses import replace

from meridianforge.engine.underwriting_engine import UnderwritingEngine
from meridianforge.models.domain.property import Property
from meridianforge.models.domain.scenario import Scenario
from meridianforge.models.results.stress_result import StressResult


class StressTestEngine:
    """
    Runs downside scenarios against properties.
    """

    @staticmethod
    def analyze(
        property_data: Property,
        scenario: Scenario,
    ) -> StressResult:
        """
        Apply scenario adjustments and compare results.
        """

        base_result = UnderwritingEngine.analyze(property_data)

        adjusted_rent = (
            property_data.income.monthly_rent
            * (1 + scenario.rent_change_percent)
            * (1 - scenario.vacancy_change_percent)
        )

        adjusted_income = replace(
            property_data.income,
            monthly_rent=adjusted_rent,
        )

        adjusted_expenses = replace(
            property_data.expenses,
            management=(
                property_data.expenses.management
                * (1 + scenario.expense_change_percent)
            ),
            maintenance=(
                property_data.expenses.maintenance
                * (1 + scenario.expense_change_percent)
            ),
            insurance=(
                property_data.expenses.insurance * (1 + scenario.expense_change_percent)
            ),
        )

        adjusted_financing = replace(
            property_data.financing,
            interest_rate=(
                property_data.financing.interest_rate
                + (scenario.interest_rate_change_percent * 100)
            ),
        )

        adjusted_property = replace(
            property_data,
            income=adjusted_income,
            expenses=adjusted_expenses,
            financing=adjusted_financing,
        )

        stressed_result = UnderwritingEngine.analyze(adjusted_property)

        return StressResult(
            scenario_name=scenario.name,
            base_result=base_result,
            stressed_result=stressed_result,
            dscr_change=(stressed_result.dscr - base_result.dscr),
            cash_flow_change=(
                stressed_result.monthly_cash_flow - base_result.monthly_cash_flow
            ),
            passed=stressed_result.dscr >= 1.20,
        )
