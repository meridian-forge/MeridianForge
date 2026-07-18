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
