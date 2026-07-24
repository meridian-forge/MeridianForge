"""
Investor lifecycle tests.

MF-346.2
"""

from meridianforge.integration.lifecycle import (
    InvestorLifecycleEngine,
)
from meridianforge.portfolio.analytics import (
    PortfolioAnalytics,
)
from meridianforge.portfolio.portfolio import (
    Portfolio,
)


def test_investor_lifecycle_identifies_growth():

    portfolio = Portfolio(
        name="Core Rentals",
        strategy="Long Term Hold",
    )

    analytics = PortfolioAnalytics(
        asset_count=3,
        total_purchase_price=600000,
        total_monthly_rent=6000,
        total_monthly_cash_flow=1800,
        annual_cash_flow=21600,
        average_cap_rate=0.08,
        average_dscr=1.5,
        portfolio_score=95,
    )

    state = InvestorLifecycleEngine.evaluate(
        portfolio,
        analytics,
    )

    assert state.status == "GROWING"

    assert state.next_action == "Evaluate next acquisition"


def test_investor_lifecycle_detects_review():

    portfolio = Portfolio(
        name="Risk Portfolio",
        strategy="Hold",
    )

    analytics = PortfolioAnalytics(
        asset_count=1,
        total_purchase_price=250000,
        total_monthly_rent=1800,
        total_monthly_cash_flow=100,
        annual_cash_flow=1200,
        average_cap_rate=0.05,
        average_dscr=1.1,
        portfolio_score=60,
    )

    state = InvestorLifecycleEngine.evaluate(
        portfolio,
        analytics,
    )

    assert state.status == "REVIEW"

    assert state.next_action == "Review portfolio risks"
