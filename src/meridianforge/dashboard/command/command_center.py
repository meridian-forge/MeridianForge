"""
Investor command center.

MF-349.3
"""

from dataclasses import dataclass

from meridianforge.dashboard.command.summary import (
    CommandCenterSummary,
)
from meridianforge.dashboard.metrics import (
    DashboardMetrics,
)
from meridianforge.dashboard.panels.actions import (
    ActionPanelItem,
)
from meridianforge.dashboard.panels.alerts import (
    AlertPanelItem,
)


@dataclass(slots=True)
class InvestorCommandCenter:
    """
    Complete investor operating view.
    """

    title: str

    summary: CommandCenterSummary

    alerts: list[AlertPanelItem]

    actions: list[ActionPanelItem]


class InvestorCommandCenterBuilder:
    """
    Aggregates dashboard components.
    """

    def build(
        self,
        metrics: DashboardMetrics,
        alerts: list[AlertPanelItem],
        actions: list[ActionPanelItem],
    ) -> InvestorCommandCenter:
        """
        Build investor command center.
        """

        if metrics.portfolio_score >= 90:
            status = "STRONG"

        elif metrics.portfolio_score >= 75:
            status = "STABLE"

        else:
            status = "REVIEW"

        summary = CommandCenterSummary(
            health_status=status,
            portfolio_score=metrics.portfolio_score,
            cash_flow_summary=(f"${metrics.monthly_cash_flow:,.0f}/month"),
            alert_count=len(alerts),
            action_count=len(actions),
        )

        return InvestorCommandCenter(
            title="Meridian Forge Investor Command Center",
            summary=summary,
            alerts=alerts,
            actions=actions,
        )
