"""
Deal scoring engine.

Ranks acquisition opportunities based on investment metrics.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class DealScore:
    """
    Represents opportunity quality score.
    """

    cash_flow_score: float
    cap_rate_score: float
    risk_score: float
    market_score: float
    overall_score: float


class DealScoreEngine:
    """
    Calculates weighted opportunity scores.
    """

    def evaluate(
        self,
        cash_flow_score: float,
        cap_rate_score: float,
        risk_score: float,
        market_score: float,
    ) -> DealScore:
        """
        Calculate weighted deal score.
        """

        overall_score = (
            cash_flow_score * 0.40
            + cap_rate_score * 0.30
            + risk_score * 0.20
            + market_score * 0.10
        )

        return DealScore(
            cash_flow_score=cash_flow_score,
            cap_rate_score=cap_rate_score,
            risk_score=risk_score,
            market_score=market_score,
            overall_score=overall_score,
        )
