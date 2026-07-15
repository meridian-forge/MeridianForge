from meridianforge.engine import StressTestEngine
from meridianforge.models.domain import Scenario
from tests.test_underwriting_engine import create_sample_property


def test_full_market_stress():

    result = StressTestEngine.analyze(
        create_sample_property(),
        Scenario(
            name="Full Market Stress",
            rent_change_percent=-0.10,
            vacancy_change_percent=0.05,
            expense_change_percent=0.25,
            interest_rate_change_percent=0.01,
        ),
    )

    assert (
        result.stressed_result.monthly_cash_flow < result.base_result.monthly_cash_flow
    )

    assert result.stressed_result.dscr < result.base_result.dscr
