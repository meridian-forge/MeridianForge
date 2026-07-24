"""
Portfolio decision engine.

MF-344.1

Produces investor-level portfolio decisions.
"""

from dataclasses import dataclass

from meridianforge.portfolio.analytics import (
    PortfolioAnalytics,
)


@dataclass(slots=True)
class PortfolioDecision:
    """
    Portfolio decision output.
    """

    decision: str

    confidence: float


class PortfolioDecisionEngine:
    """
    Determines portfolio management decisions.
    """

    @staticmethod
    def evaluate(
        analytics: PortfolioAnalytics,
    ) -> PortfolioDecision:
        """
        Evaluate portfolio condition.
        """

        if analytics.portfolio_score >= 90 and analytics.average_dscr >= 1.5:
            return PortfolioDecision(
                decision="HOLD_AND_SCALE",
                confidence=0.95,
            )

        if analytics.portfolio_score >= 75:
            return PortfolioDecision(
                decision="MONITOR",
                confidence=0.80,
            )

        return PortfolioDecision(
            decision="REBALANCE",
            confidence=0.90,
        )
