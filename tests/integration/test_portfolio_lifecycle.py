"""
Portfolio lifecycle integration test.

MF-342.3

Validates:

Acquisition Result
        |
Portfolio
        |
Analytics
        |
Dashboard
"""

from meridianforge.portfolio.analytics import (
    PortfolioAnalyticsEngine,
)
from meridianforge.portfolio.dashboard import (
    PortfolioDashboardBuilder,
)
from meridianforge.portfolio.portfolio import (
    Portfolio,
)


class MockAsset:
    def __init__(self):
        self.purchase_price = 200000
        self.monthly_rent = 2000
        self.monthly_cash_flow = 500
        self.cap_rate = 0.08
        self.dscr = 1.5
        self.score = 90


def test_portfolio_lifecycle():

    portfolio = Portfolio(
        name="Core Rentals",
        strategy="Long Term Hold",
    )

    portfolio.add_asset(MockAsset())

    analytics = PortfolioAnalyticsEngine.analyze(portfolio)

    dashboard = PortfolioDashboardBuilder.build(
        portfolio,
        analytics,
    )

    assert analytics.asset_count == 1
    assert dashboard.portfolio_name == "Core Rentals"
