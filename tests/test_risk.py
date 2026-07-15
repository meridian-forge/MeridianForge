from meridianforge.engine import RiskEngine, StressTestEngine
from meridianforge.models.domain import Scenario
from meridianforge.models.results import RiskRating
from tests.test_underwriting_engine import create_sample_property


def test_safe_scenario():

    result = StressTestEngine.analyze(
        create_sample_property(),
        Scenario(
            name="Small Rent Drop",
            rent_change_percent=-0.02,
        ),
    )

    rating = RiskEngine.evaluate(result)

    assert rating == RiskRating.SAFE


def test_warning_scenario():

    result = StressTestEngine.analyze(
        create_sample_property(),
        Scenario(
            name="Major Market Stress",
            rent_change_percent=-0.15,
            expense_change_percent=0.50,
        ),
    )

    rating = RiskEngine.evaluate(result)

    assert rating in (
        RiskRating.WARNING,
        RiskRating.CRITICAL,
    )
