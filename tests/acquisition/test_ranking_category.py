from meridianforge.acquisition.ranking_category import (
    classify_rank_score,
)


def test_ranking_categories():

    assert classify_rank_score(95) == "A+"

    assert classify_rank_score(85) == "A"

    assert classify_rank_score(75) == "B"

    assert classify_rank_score(65) == "C"

    assert classify_rank_score(50) == "D"
