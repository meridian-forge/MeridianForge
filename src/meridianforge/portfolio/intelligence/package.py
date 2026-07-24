"""
Investor decision package.

MF-344.3

Combines portfolio intelligence outputs
into a single investor-facing decision object.
"""

from dataclasses import dataclass

from meridianforge.portfolio.intelligence.action import (
    PortfolioAction,
)
from meridianforge.portfolio.intelligence.decision import (
    PortfolioDecision,
)
from meridianforge.portfolio.intelligence.health import (
    PortfolioHealth,
)
from meridianforge.portfolio.intelligence.ranking import (
    PortfolioRanking,
)
from meridianforge.portfolio.intelligence.recommendation import (
    PortfolioRecommendation,
)


@dataclass(slots=True)
class InvestorDecisionPackage:
    """
    Complete portfolio intelligence package.
    """

    health: PortfolioHealth

    recommendation: PortfolioRecommendation

    ranking: PortfolioRanking

    decision: PortfolioDecision

    action: PortfolioAction

    def summary(self) -> dict[str, object]:
        """
        Return investor summary payload.
        """

        return {
            "health_status": self.health.status,
            "health_score": self.health.score,
            "recommendation": self.recommendation.action,
            "priority": self.ranking.priority,
            "decision": self.decision.decision,
            "action": self.action.action,
            "urgency": self.action.urgency,
        }


class InvestorDecisionPackageBuilder:
    """
    Builds complete investor decision packages.
    """

    @staticmethod
    def build(
        health: PortfolioHealth,
        recommendation: PortfolioRecommendation,
        ranking: PortfolioRanking,
        decision: PortfolioDecision,
        action: PortfolioAction,
    ) -> InvestorDecisionPackage:
        """
        Assemble investor decision package.
        """

        return InvestorDecisionPackage(
            health=health,
            recommendation=recommendation,
            ranking=ranking,
            decision=decision,
            action=action,
        )
