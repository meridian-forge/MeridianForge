"""
Tests for deal scoring engine.
"""

from meridianforge.scoring.deal_score_engine import (
    DealScoreEngine,
)


def test_deal_score_engine_calculates_weighted_score() -> None:
    """
    Validate weighted deal scoring.
    """

    score = DealScoreEngine().evaluate(
        cash_flow_score=0.90,
        cap_rate_score=0.80,
        risk_score=0.70,
        market_score=0.60,
    )

    assert score.cash_flow_score == 0.90
    assert score.overall_score == 0.80
