"""
Investor dashboard builder.

MF-349.1
"""

from dataclasses import dataclass

from meridianforge.dashboard.metrics import (
    DashboardMetrics,
)
from meridianforge.dashboard.widgets import (
    DashboardWidget,
    DashboardWidgetBuilder,
)


@dataclass(slots=True)
class InvestorDashboard:
    """
    Investor dashboard output.
    """

    title: str

    metrics: DashboardMetrics

    widgets: list[DashboardWidget]


class InvestorDashboardBuilder:
    """
    Builds investor dashboard summaries.
    """

    def build(
        self,
        metrics: DashboardMetrics,
    ) -> InvestorDashboard:
        """
        Generate investor dashboard.
        """

        widgets = [
            DashboardWidgetBuilder.health(
                metrics.portfolio_score,
            ),
            DashboardWidgetBuilder.cash_flow(
                metrics.monthly_cash_flow,
            ),
        ]

        return InvestorDashboard(
            title="Meridian Forge Investor Dashboard",
            metrics=metrics,
            widgets=widgets,
        )
