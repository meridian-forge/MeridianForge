"""
MF-206.0 Intelligence Scoring Engine.

Combines weighted investment factors into a normalized score.
"""

from .factors import ScoringFactors
from .weights import ScoringWeights


class IntelligenceScoringEngine:
    def __init__(
        self,
        weights: ScoringWeights | None = None,
    ) -> None:
        self.weights = weights or ScoringWeights()

    def calculate_score(
        self,
        factors: ScoringFactors,
    ) -> float:
        score = (
            factors.cash_flow * self.weights.cash_flow
            + factors.appreciation * self.weights.appreciation
            + factors.risk * self.weights.risk
            + factors.tax_efficiency * self.weights.tax_efficiency
            + factors.liquidity * self.weights.liquidity
        )

        return round(score, 2)
