from dataclasses import dataclass

from meridianforge.portfolio.analytics import (
    PortfolioAnalyticsEngine,
)

from meridianforge.portfolio.dashboard import (
    PortfolioDashboardBuilder,
)

from meridianforge.portfolio.portfolio import (
    Portfolio,
)


@dataclass
class MockAsset:

    purchase_price: float

    monthly_rent: float

    monthly_cash_flow: float

    cap_rate: float

    dscr: float

    score: float


def test_portfolio_dashboard_creation():

    portfolio = Portfolio(
        name="Core Rentals",
        strategy="Long Term Hold",
    )

    portfolio.add_asset(
        MockAsset(
            purchase_price=200000,
            monthly_rent=2000,
            monthly_cash_flow=500,
            cap_rate=0.08,
            dscr=1.5,
            score=90,
        )
    )

    analytics = PortfolioAnalyticsEngine.analyze(
        portfolio,
    )

    dashboard = PortfolioDashboardBuilder.build(
        portfolio,
        analytics,
    )

    assert dashboard.portfolio_name == "Core Rentals"
    assert dashboard.asset_count == 1
    assert dashboard.status == "STRONG"
    assert dashboard.monthly_cash_flow == 500
