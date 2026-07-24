"""
Investor Command Center.

MF-347.1

Aggregates investor position,
portfolio intelligence, and next actions.
"""

from dataclasses import dataclass

from meridianforge.investor.profile import (
    InvestorProfile,
)
from meridianforge.portfolio.dashboard import (
    PortfolioDashboard,
)


@dataclass(slots=True)
class InvestorCommandCenter:
    """
    Investor operating summary.
    """

    investor_name: str

    portfolio_status: str

    monthly_cash_flow: float

    asset_count: int

    recommended_action: str


class InvestorCommandCenterBuilder:
    """
    Builds investor operating view.
    """

    @staticmethod
    def build(
        profile: InvestorProfile,
        dashboard: PortfolioDashboard,
    ) -> InvestorCommandCenter:
        """
        Convert portfolio dashboard into
        investor command center.
        """

        if dashboard.status == "STRONG":
            action = "Evaluate next acquisition"

        elif dashboard.status == "GOOD":
            action = "Optimize current portfolio"

        else:
            action = "Review portfolio risks"

        return InvestorCommandCenter(
            investor_name=profile.name,
            portfolio_status=dashboard.status,
            monthly_cash_flow=dashboard.monthly_cash_flow,
            asset_count=dashboard.asset_count,
            recommended_action=action,
        )
