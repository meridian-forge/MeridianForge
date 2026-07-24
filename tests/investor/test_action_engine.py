"""
Investor action engine tests.

MF-347.2
"""

from meridianforge.investor.action_engine import (
    InvestorActionEngine,
)
from meridianforge.portfolio.dashboard import (
    PortfolioDashboard,
)


def test_strong_portfolio_generates_growth_actions():

    dashboard = PortfolioDashboard(
        portfolio_name="Core Rentals",
        strategy="Hold",
        asset_count=5,
        total_investment=1000000,
        monthly_rent=10000,
        monthly_cash_flow=3000,
        annual_cash_flow=36000,
        average_cap_rate=0.08,
        average_dscr=1.5,
        portfolio_score=95,
        status="STRONG",
    )

    plan = InvestorActionEngine.generate_plan(
        dashboard,
    )

    assert len(plan.actions) == 2

    assert plan.actions[0].title == "Acquire next property"
