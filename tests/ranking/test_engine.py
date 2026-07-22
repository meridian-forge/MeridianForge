from meridianforge.ranking.engine import calculate_score
from meridianforge.ranking.models import RankingInput


def test_score_calculation() -> None:
    result = RankingInput(
        opportunity_file="property.xlsx",
        metrics={
            "cash_on_cash": 0.12,
            "dscr": 1.35,
        },
    )

    score = calculate_score(result)

    assert score > 60
