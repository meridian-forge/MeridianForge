"""
Portfolio health intelligence tests.

MF-344.1
"""

from meridianforge.portfolio.analytics import (
    PortfolioAnalytics,
)
from meridianforge.portfolio.intelligence.health import (
    PortfolioHealthEngine,
)


def test_portfolio_health_identifies_strong_portfolio():

    analytics = PortfolioAnalytics(
        asset_count=5,
        total_purchase_price=1000000,
        total_monthly_rent=10000,
        total_monthly_cash_flow=3000,
        annual_cash_flow=36000,
        average_cap_rate=0.08,
        average_dscr=1.6,
        portfolio_score=92,
    )

    health = PortfolioHealthEngine.analyze(
        analytics,
    )

    assert health.status == "STRONG"

    assert health.score == 100

    assert "Strong debt coverage ratio" in health.strengths

    assert len(health.recommendations) > 0


def test_portfolio_health_detects_risk():

    analytics = PortfolioAnalytics(
        asset_count=1,
        total_purchase_price=250000,
        total_monthly_rent=2000,
        total_monthly_cash_flow=100,
        annual_cash_flow=1200,
        average_cap_rate=0.05,
        average_dscr=1.1,
        portfolio_score=70,
    )

    health = PortfolioHealthEngine.analyze(
        analytics,
    )

    assert health.status == "NEEDS_ATTENTION"

    assert len(health.risks) > 0
