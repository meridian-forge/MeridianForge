from meridianforge.models.results.acquisition_assessment import (
    AcquisitionAssessment,
)
from meridianforge.services.recommendation_engine import (
    RecommendationEngine,
)


def test_buy_recommendation() -> None:

    assessment = AcquisitionAssessment(
        dscr=1.35,
        monthly_cash_flow=350,
        cap_rate=0.07,
    )

    result = RecommendationEngine.evaluate(
        assessment,
    )

    assert result.decision == "BUY"


def test_pass_recommendation() -> None:

    assessment = AcquisitionAssessment(
        dscr=0.9,
        monthly_cash_flow=-100,
        cap_rate=0.03,
    )

    result = RecommendationEngine.evaluate(
        assessment,
    )

    assert result.decision == "PASS"
