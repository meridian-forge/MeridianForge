"""
Investor action engine.

MF-347.2

Transforms portfolio intelligence
into investor operating tasks.
"""

from meridianforge.investor.action_plan import (
    InvestorAction,
    InvestorActionPlan,
)
from meridianforge.investor.alerts import (
    InvestorAlert,
)
from meridianforge.portfolio.dashboard import (
    PortfolioDashboard,
)


class InvestorActionEngine:
    """
    Generates investor actions and alerts.
    """

    @staticmethod
    def generate_plan(
        dashboard: PortfolioDashboard,
    ) -> InvestorActionPlan:
        """
        Generate recommended actions.
        """

        actions: list[InvestorAction] = []

        if dashboard.status == "STRONG":
            actions.append(
                InvestorAction(
                    priority=1,
                    title="Acquire next property",
                    reason=("Portfolio health supports expansion"),
                )
            )

            actions.append(
                InvestorAction(
                    priority=2,
                    title="Review available capital",
                    reason=("Healthy portfolio may support leverage"),
                )
            )

        elif dashboard.status == "GOOD":
            actions.append(
                InvestorAction(
                    priority=1,
                    title="Optimize current holdings",
                    reason=("Portfolio performance can improve"),
                )
            )

        else:
            actions.append(
                InvestorAction(
                    priority=1,
                    title="Review portfolio risks",
                    reason=("Portfolio requires attention"),
                )
            )

        return InvestorActionPlan(
            actions=actions,
        )

    @staticmethod
    def generate_alerts(
        dashboard: PortfolioDashboard,
    ) -> list[InvestorAlert]:
        """
        Generate portfolio alerts.
        """

        alerts: list[InvestorAlert] = []

        if dashboard.status == "REVIEW":
            alerts.append(
                InvestorAlert(
                    severity="HIGH",
                    title="Portfolio Review Required",
                    message=("Portfolio health requires investor attention"),
                )
            )

        elif dashboard.average_dscr < 1.20:
            alerts.append(
                InvestorAlert(
                    severity="MEDIUM",
                    title="Debt Coverage Warning",
                    message=("DSCR has fallen below target"),
                )
            )

        return alerts
