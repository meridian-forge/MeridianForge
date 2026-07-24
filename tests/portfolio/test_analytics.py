from dataclasses import dataclass

import pytest

from meridianforge.portfolio.analytics import (
    PortfolioAnalyticsEngine,
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


def test_portfolio_analytics_calculates_metrics():

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

    portfolio.add_asset(
        MockAsset(
            purchase_price=300000,
            monthly_rent=3000,
            monthly_cash_flow=700,
            cap_rate=0.07,
            dscr=1.6,
            score=95,
        )
    )

    analytics = PortfolioAnalyticsEngine.analyze(
        portfolio,
    )

    assert analytics.asset_count == 2
    assert analytics.total_purchase_price == 500000
    assert analytics.total_monthly_rent == 5000
    assert analytics.annual_cash_flow == 14400

    assert analytics.average_cap_rate == pytest.approx(
        0.075,
    )

    assert analytics.average_dscr == pytest.approx(
        1.55,
    )

    assert analytics.portfolio_score == pytest.approx(
        92.5,
    )


def test_empty_portfolio_returns_zero_metrics():

    portfolio = Portfolio(
        name="Empty",
        strategy="Hold",
    )

    analytics = PortfolioAnalyticsEngine.analyze(
        portfolio,
    )

    assert analytics.asset_count == 0
    assert analytics.portfolio_score == 0.0
