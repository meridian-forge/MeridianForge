"""
Weekly investor review tests.

MF-345.1
"""

from meridianforge.portfolio.intelligence.dashboard import (
    InvestorDashboard,
)
from meridianforge.portfolio.intelligence.review import (
    WeeklyInvestorReviewBuilder,
)


def test_weekly_investor_review():

    dashboard = InvestorDashboard(
        status="STRONG",
        health_score=95,
        priority="HIGH",
        decision="HOLD_AND_SCALE",
        recommended_action="Acquire assets",
        urgency="NORMAL",
        highlights=[
            "Strong portfolio",
        ],
        concerns=[],
    )

    review = WeeklyInvestorReviewBuilder.build(
        dashboard,
    )

    assert review.title == ("Meridian Forge Weekly Investor Review")

    assert "HOLD_AND_SCALE" in review.summary

    assert len(review.action_items) == 1
