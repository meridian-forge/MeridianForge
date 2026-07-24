"""
Portfolio action tests.

MF-344.2
"""

from meridianforge.portfolio.intelligence.action import (
    PortfolioActionEngine,
)
from meridianforge.portfolio.intelligence.decision import (
    PortfolioDecision,
)
from meridianforge.portfolio.intelligence.recommendation import (
    PortfolioRecommendation,
)


def test_portfolio_action_generation():

    decision = PortfolioDecision(
        decision="HOLD_AND_SCALE",
        confidence=0.95,
    )

    recommendation = PortfolioRecommendation(
        action="ACQUIRE",
        rationale=[
            "Strong portfolio",
        ],
    )

    result = PortfolioActionEngine.generate(
        decision,
        recommendation,
    )

    assert result.action == "Acquire additional assets"
    assert result.urgency == "NORMAL"
