"""
Deal evaluation model tests.
"""

from meridianforge.models.results.deal_evaluation import (
    DealEvaluation,
)


def test_deal_evaluation_creation() -> None:
    """
    Verify deal evaluation creation.
    """

    result = DealEvaluation(
        qualified=True,
        score=100,
        reasons=[
            "DSCR requirement met",
        ],
    )

    assert result.qualified is True

    assert result.score == 100

    assert result.reasons == [
        "DSCR requirement met",
    ]
