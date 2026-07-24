"""
Investor dashboard widgets.

MF-349.1
"""

from dataclasses import dataclass


@dataclass(slots=True)
class DashboardWidget:
    """
    Generic dashboard component.
    """

    title: str

    value: str

    status: str


class DashboardWidgetBuilder:
    """
    Builds investor dashboard widgets.
    """

    @staticmethod
    def health(
        score: float,
    ) -> DashboardWidget:
        """
        Create portfolio health widget.
        """

        if score >= 90:
            status = "STRONG"

        elif score >= 75:
            status = "STABLE"

        else:
            status = "REVIEW"

        return DashboardWidget(
            title="Portfolio Health",
            value=f"{score:.1f}",
            status=status,
        )

    @staticmethod
    def cash_flow(
        monthly_cash_flow: float,
    ) -> DashboardWidget:
        """
        Create cash flow widget.
        """

        return DashboardWidget(
            title="Monthly Cash Flow",
            value=f"${monthly_cash_flow:,.0f}",
            status="ACTIVE",
        )
