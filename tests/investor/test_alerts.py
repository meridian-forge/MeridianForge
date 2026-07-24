"""
Investor alert tests.

MF-347.2
"""

from meridianforge.investor.action_engine import (
    InvestorActionEngine,
)
from meridianforge.portfolio.dashboard import (
    PortfolioDashboard,
)


def test_risk_portfolio_generates_alert():

    dashboard = PortfolioDashboard(
        portfolio_name="Risk Portfolio",
        strategy="Hold",
        asset_count=1,
        total_investment=250000,
        monthly_rent=2000,
        monthly_cash_flow=100,
        annual_cash_flow=1200,
        average_cap_rate=0.05,
        average_dscr=1.1,
        portfolio_score=60,
        status="REVIEW",
    )

    alerts = InvestorActionEngine.generate_alerts(
        dashboard,
    )

    assert len(alerts) == 1

    assert alerts[0].severity == "HIGH"
