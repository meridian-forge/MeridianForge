from meridianforge.engine import StressTestEngine
from meridianforge.models.domain import Scenario
from tests.test_underwriting_engine import create_sample_property


def test_rent_drop_scenario():

    property_data = create_sample_property()

    scenario = Scenario(
        name="10% Rent Drop",
        rent_change_percent=-0.10,
    )

    result = StressTestEngine.analyze(
        property_data,
        scenario,
    )

    assert result.scenario_name == "10% Rent Drop"

    assert result.stressed_result.monthly_cash_flow < (
        result.base_result.monthly_cash_flow
    )

    assert result.dscr_change < 0
