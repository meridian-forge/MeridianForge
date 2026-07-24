"""
Portfolio recommendation tests.
"""

from meridianforge.portfolio.analytics import (
    PortfolioAnalytics,
)
from meridianforge.portfolio.intelligence.recommendation import (
    PortfolioRecommendationEngine,
)


def test_portfolio_recommendation_engine():

    analytics = PortfolioAnalytics(
        asset_count=2,
        total_purchase_price=500000,
        total_monthly_rent=5000,
        total_monthly_cash_flow=1200,
        annual_cash_flow=14400,
        average_cap_rate=0.075,
        average_dscr=1.55,
        portfolio_score=92.5,
    )

    result = PortfolioRecommendationEngine.analyze(
        analytics,
    )

    assert result.action == "ACQUIRE"
    assert len(result.rationale) > 0
