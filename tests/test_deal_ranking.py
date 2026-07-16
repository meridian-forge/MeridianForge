"""
Deal ranking tests.
"""

from meridianforge.engine.deal_ranking import (
    DealRankingEngine,
)
from meridianforge.models.results.deal_evaluation import (
    DealEvaluation,
)
from tests.test_criteria_engine import (
    create_sample_property,
)


def test_ranking_orders_by_score() -> None:
    """
    Highest score should rank first.
    """

    property_a = create_sample_property()
    property_b = create_sample_property()

    low = DealEvaluation(
        qualified=True,
        score=72,
        reasons=[],
        failed_criteria=[],
    )

    high = DealEvaluation(
        qualified=True,
        score=95,
        reasons=[],
        failed_criteria=[],
    )

    ranked = DealRankingEngine.rank(
        [
            (property_a, low),
            (property_b, high),
        ]
    )

    assert ranked[0].evaluation.score == 95
    assert ranked[0].rank == 1

    assert ranked[1].evaluation.score == 72
    assert ranked[1].rank == 2
