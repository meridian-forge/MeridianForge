"""
Investor dashboard tests.

MF-345.1
"""

from meridianforge.portfolio.intelligence.action import (
    PortfolioAction,
)
from meridianforge.portfolio.intelligence.dashboard import (
    InvestorDashboardBuilder,
)
from meridianforge.portfolio.intelligence.decision import (
    PortfolioDecision,
)
from meridianforge.portfolio.intelligence.health import (
    PortfolioHealth,
)
from meridianforge.portfolio.intelligence.package import (
    InvestorDecisionPackageBuilder,
)
from meridianforge.portfolio.intelligence.ranking import (
    PortfolioRanking,
)
from meridianforge.portfolio.intelligence.recommendation import (
    PortfolioRecommendation,
)


def test_investor_dashboard_creation():

    package = InvestorDecisionPackageBuilder.build(
        PortfolioHealth(
            status="STRONG",
            score=95,
            strengths=["Strong cash flow"],
            risks=[],
            recommendations=["Scale"],
        ),
        PortfolioRecommendation(
            action="ACQUIRE",
            rationale=["Growth"],
        ),
        PortfolioRanking(
            priority="HIGH",
            score=95,
            rationale=["Quality"],
        ),
        PortfolioDecision(
            decision="HOLD_AND_SCALE",
            confidence=0.95,
        ),
        PortfolioAction(
            action="Acquire assets",
            urgency="NORMAL",
            explanation="Scale",
        ),
    )

    dashboard = InvestorDashboardBuilder.build(
        package,
    )

    assert dashboard.status == "STRONG"

    assert dashboard.priority == "HIGH"

    assert dashboard.decision == "HOLD_AND_SCALE"
