from meridianforge.dashboard.command.command_center import (
    InvestorCommandCenterBuilder,
)
from meridianforge.dashboard.metrics import (
    DashboardMetrics,
)


def test_command_center_builds():

    metrics = DashboardMetrics(
        portfolio_score=95,
        asset_count=5,
        monthly_cash_flow=5000,
        annual_cash_flow=60000,
        average_cap_rate=0.06,
        average_dscr=1.5,
        active_alerts=1,
        pending_actions=2,
    )

    center = InvestorCommandCenterBuilder().build(
        metrics,
        [],
        [],
    )

    assert center.title == "Meridian Forge Investor Command Center"

    assert center.summary.health_status == "STRONG"
