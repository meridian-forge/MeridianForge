"""
Portfolio decision tests.
"""

from meridianforge.portfolio.analytics import (
    PortfolioAnalytics,
)
from meridianforge.portfolio.intelligence.decision import (
    PortfolioDecisionEngine,
)


def test_portfolio_decision_engine():

    analytics = PortfolioAnalytics(
        asset_count=3,
        total_purchase_price=750000,
        total_monthly_rent=7500,
        total_monthly_cash_flow=2000,
        annual_cash_flow=24000,
        average_cap_rate=0.08,
        average_dscr=1.6,
        portfolio_score=95,
    )

    result = PortfolioDecisionEngine.evaluate(
        analytics,
    )

    assert result.decision == "HOLD_AND_SCALE"
    assert result.confidence == 0.95
