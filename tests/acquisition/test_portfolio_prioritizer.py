from meridianforge.acquisition.portfolio_prioritizer import (
    PortfolioPrioritizer,
)
from meridianforge.acquisition.ranking_model import (
    RankingResult,
)


def test_portfolio_prioritizer_actions():

    rankings = [
        RankingResult(
            property_address="A",
            rank=1,
            score=95,
            category="A+",
            recommendation="BUY",
        ),
        RankingResult(
            property_address="B",
            rank=2,
            score=75,
            category="B",
            recommendation="REVIEW",
        ),
        RankingResult(
            property_address="C",
            rank=3,
            score=55,
            category="D",
            recommendation="REVIEW",
        ),
    ]

    result = PortfolioPrioritizer.prioritize(rankings)

    assert result[0].action == "BUY NOW"

    assert result[1].action == "REVIEW"

    assert result[2].action == "REJECT"
