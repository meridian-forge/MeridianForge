from meridianforge.dashboard.investor_dashboard import (
    InvestorDashboardBuilder,
)
from meridianforge.dashboard.metrics import (
    DashboardMetrics,
)


def test_dashboard_builds():

    metrics = DashboardMetrics(
        portfolio_score=90,
        asset_count=3,
        monthly_cash_flow=5000,
        annual_cash_flow=60000,
        average_cap_rate=0.06,
        average_dscr=1.5,
        active_alerts=1,
        pending_actions=2,
    )

    dashboard = InvestorDashboardBuilder().build(
        metrics,
    )

    assert dashboard.title == "Meridian Forge Investor Dashboard"

    assert len(dashboard.widgets) == 2
