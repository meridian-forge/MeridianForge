from meridianforge.intelligence.recommendation.engine import (
    recommend,
)


def test_buy_recommendation() -> None:

    result = recommend(
        cash_flow=300,
        dscr=1.35,
        appreciation_score=80,
    )

    assert result.action == "BUY"


def test_pass_recommendation() -> None:

    result = recommend(
        cash_flow=-100,
        dscr=0.8,
        appreciation_score=40,
    )

    assert result.action == "PASS"
