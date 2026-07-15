from meridianforge.models.domain import Scenario


def test_scenario_creation():

    scenario = Scenario(
        name="Market Downturn",
        rent_change_percent=-0.10,
        expense_change_percent=0.20,
        interest_rate_change_percent=0.01,
    )

    assert scenario.name == "Market Downturn"

    assert scenario.rent_change_percent == -0.10

    assert scenario.expense_change_percent == 0.20

    assert scenario.interest_rate_change_percent == 0.01
