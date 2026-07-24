"""
Investor decision package tests.

MF-344.3
"""

from meridianforge.portfolio.intelligence.action import (
    PortfolioAction,
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


def test_investor_decision_package_builder():

    health = PortfolioHealth(
        status="STRONG",
        score=100,
        strengths=[
            "Strong cash flow",
        ],
        risks=[],
        recommendations=[
            "Scale portfolio",
        ],
    )

    recommendation = PortfolioRecommendation(
        action="ACQUIRE",
        rationale=[
            "Expansion recommended",
        ],
    )

    ranking = PortfolioRanking(
        priority="HIGH",
        score=95,
        rationale=[
            "Strong fundamentals",
        ],
    )

    decision = PortfolioDecision(
        decision="HOLD_AND_SCALE",
        confidence=0.95,
    )

    action = PortfolioAction(
        action="Acquire additional assets",
        urgency="NORMAL",
        explanation="Portfolio supports expansion.",
    )

    package = InvestorDecisionPackageBuilder.build(
        health,
        recommendation,
        ranking,
        decision,
        action,
    )

    summary = package.summary()

    assert summary["health_status"] == "STRONG"

    assert summary["recommendation"] == "ACQUIRE"

    assert summary["decision"] == "HOLD_AND_SCALE"

    assert summary["action"] == "Acquire additional assets"
