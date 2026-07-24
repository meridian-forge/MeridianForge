"""
Portfolio investor action engine.

MF-344.2

Converts portfolio intelligence into
recommended investor actions.
"""

from dataclasses import dataclass

from meridianforge.portfolio.intelligence.decision import (
    PortfolioDecision,
)
from meridianforge.portfolio.intelligence.recommendation import (
    PortfolioRecommendation,
)


@dataclass(slots=True)
class PortfolioAction:
    """
    Investor action output.
    """

    action: str

    urgency: str

    explanation: str


class PortfolioActionEngine:
    """
    Creates investor-facing actions.
    """

    @staticmethod
    def generate(
        decision: PortfolioDecision,
        recommendation: PortfolioRecommendation,
    ) -> PortfolioAction:
        """
        Convert intelligence into action.
        """

        if decision.decision == "HOLD_AND_SCALE":

            return PortfolioAction(
                action="Acquire additional assets",
                urgency="NORMAL",
                explanation=("Portfolio fundamentals support continued expansion."),
            )

        if decision.decision == "REBALANCE":

            return PortfolioAction(
                action="Review portfolio restructuring",
                urgency="HIGH",
                explanation=("Portfolio metrics indicate corrective action."),
            )

        return PortfolioAction(
            action=recommendation.action,
            urgency="LOW",
            explanation=("Continue monitoring portfolio performance."),
        )
