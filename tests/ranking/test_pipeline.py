from meridianforge.ranking.pipeline import (
    RankingPipeline,
)


def test_ranking_orders_highest_score_first() -> None:

    pipeline = RankingPipeline()

    opportunities = [
        {
            "name": "Property A",
            "score": 70,
        },
        {
            "name": "Property B",
            "score": 90,
        },
        {
            "name": "Property C",
            "score": 80,
        },
    ]

    ranked = pipeline.rank(opportunities)

    assert ranked[0]["name"] == "Property B"
    assert ranked[1]["name"] == "Property C"
    assert ranked[2]["name"] == "Property A"
