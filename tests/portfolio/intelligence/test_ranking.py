"""
Portfolio ranking tests.

MF-344.2
"""

from meridianforge.portfolio.analytics import (
    PortfolioAnalytics,
)
from meridianforge.portfolio.intelligence.ranking import (
    PortfolioRankingEngine,
)


def test_portfolio_ranking_high_priority():

    analytics = PortfolioAnalytics(
        asset_count=5,
        total_purchase_price=1000000,
        total_monthly_rent=10000,
        total_monthly_cash_flow=3000,
        annual_cash_flow=36000,
        average_cap_rate=0.08,
        average_dscr=1.6,
        portfolio_score=95,
    )

    result = PortfolioRankingEngine.rank(
        analytics,
    )

    assert result.priority == "HIGH"
    assert result.score >= 85
