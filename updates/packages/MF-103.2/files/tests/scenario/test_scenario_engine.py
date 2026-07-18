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
