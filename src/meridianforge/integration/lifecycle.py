"""
Investor lifecycle engine.

MF-346.2

Manages the transition from acquisition
through portfolio ownership and review.
"""

from dataclasses import dataclass

from meridianforge.portfolio.analytics import (
    PortfolioAnalytics,
)
from meridianforge.portfolio.portfolio import (
    Portfolio,
)


@dataclass(slots=True)
class InvestorLifecycleState:
    """
    Current investor lifecycle state.
    """

    portfolio_name: str

    status: str

    health_score: float

    asset_count: int

    next_action: str


class InvestorLifecycleEngine:
    """
    Evaluates portfolio lifecycle state.
    """

    @staticmethod
    def evaluate(
        portfolio: Portfolio,
        analytics: PortfolioAnalytics,
    ) -> InvestorLifecycleState:
        """
        Generate lifecycle state.
        """

        if analytics.portfolio_score >= 90:
            status = "GROWING"

            next_action = "Evaluate next acquisition"

        elif analytics.portfolio_score >= 75:
            status = "STABLE"

            next_action = "Optimize current holdings"

        else:
            status = "REVIEW"

            next_action = "Review portfolio risks"

        return InvestorLifecycleState(
            portfolio_name=portfolio.name,
            status=status,
            health_score=analytics.portfolio_score,
            asset_count=analytics.asset_count,
            next_action=next_action,
        )
