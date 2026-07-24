"""
Portfolio analytics service.

MF-342.1

Calculates investor-level portfolio performance metrics
from the portfolio aggregate.
"""

from dataclasses import dataclass

from meridianforge.portfolio.portfolio import (
    Portfolio,
)


@dataclass(slots=True)
class PortfolioAnalytics:
    """
    Portfolio analytics output.
    """

    asset_count: int

    total_purchase_price: float

    total_monthly_rent: float

    total_monthly_cash_flow: float

    annual_cash_flow: float

    average_cap_rate: float

    average_dscr: float

    portfolio_score: float


class PortfolioAnalyticsEngine:
    """
    Calculates portfolio-level investment metrics.
    """

    @staticmethod
    def analyze(
        portfolio: Portfolio,
    ) -> PortfolioAnalytics:
        """
        Generate portfolio analytics.
        """

        assets = portfolio.assets

        if not assets:
            return PortfolioAnalytics(
                asset_count=0,
                total_purchase_price=0.0,
                total_monthly_rent=0.0,
                total_monthly_cash_flow=0.0,
                annual_cash_flow=0.0,
                average_cap_rate=0.0,
                average_dscr=0.0,
                portfolio_score=0.0,
            )

        purchase_price = sum(
            getattr(
                asset,
                "purchase_price",
                0.0,
            )
            for asset in assets
        )

        monthly_rent = sum(
            getattr(
                asset,
                "monthly_rent",
                0.0,
            )
            for asset in assets
        )

        monthly_cash_flow = sum(
            getattr(
                asset,
                "monthly_cash_flow",
                0.0,
            )
            for asset in assets
        )

        cap_rates = [
            getattr(
                asset,
                "cap_rate",
                0.0,
            )
            for asset in assets
        ]

        dscr_values = [
            getattr(
                asset,
                "dscr",
                0.0,
            )
            for asset in assets
        ]

        scores = [
            getattr(
                asset,
                "score",
                0.0,
            )
            for asset in assets
        ]

        count = len(assets)

        return PortfolioAnalytics(
            asset_count=count,
            total_purchase_price=purchase_price,
            total_monthly_rent=monthly_rent,
            total_monthly_cash_flow=monthly_cash_flow,
            annual_cash_flow=monthly_cash_flow * 12,
            average_cap_rate=sum(cap_rates) / count,
            average_dscr=sum(dscr_values) / count,
            portfolio_score=sum(scores) / count,
        )
