"""
Portfolio dashboard model.

MF-342.2

Investor-facing summary layer built
from portfolio analytics.
"""

from dataclasses import dataclass

from meridianforge.portfolio.analytics import (
    PortfolioAnalytics,
)
from meridianforge.portfolio.portfolio import (
    Portfolio,
)


@dataclass(slots=True)
class PortfolioDashboard:

    portfolio_name: str

    strategy: str

    asset_count: int

    total_investment: float

    monthly_rent: float

    monthly_cash_flow: float

    annual_cash_flow: float

    average_cap_rate: float

    average_dscr: float

    portfolio_score: float

    status: str


class PortfolioDashboardBuilder:
    """
    Converts portfolio analytics into dashboard output.
    """

    @staticmethod
    def build(
        portfolio: Portfolio,
        analytics: PortfolioAnalytics,
    ) -> PortfolioDashboard:
        """
        Build investor dashboard summary.
        """

        if analytics.portfolio_score >= 90:
            status = "STRONG"

        elif analytics.portfolio_score >= 75:
            status = "GOOD"

        else:
            status = "REVIEW"

        return PortfolioDashboard(
            portfolio_name=portfolio.name,
            strategy=portfolio.strategy,
            asset_count=analytics.asset_count,
            total_investment=analytics.total_purchase_price,
            monthly_rent=analytics.total_monthly_rent,
            monthly_cash_flow=analytics.total_monthly_cash_flow,
            annual_cash_flow=analytics.annual_cash_flow,
            average_cap_rate=analytics.average_cap_rate,
            average_dscr=analytics.average_dscr,
            portfolio_score=analytics.portfolio_score,
            status=status,
        )
