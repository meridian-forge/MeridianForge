from meridianforge.acquisition.ranking_model import (
    RankingResult,
)


def test_ranking_result_creation():

    result = RankingResult(
        property_address="123 Main",
        rank=1,
        score=95,
        category="A+",
        recommendation="BUY",
    )

    assert result.rank == 1
    assert result.category == "A+"
    assert result.recommendation == "BUY"
