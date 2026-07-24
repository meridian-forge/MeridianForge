"""
Acquisition to portfolio integration bridge.

MF-346.1

Connects approved acquisition opportunities
to portfolio management.
"""

from dataclasses import dataclass

from meridianforge.acquisition.result import (
    AcquisitionResult,
)
from meridianforge.portfolio.portfolio import (
    Portfolio,
)


@dataclass(slots=True)
class PortfolioAsset:
    """
    Portfolio representation of an acquired asset.
    """

    address: str

    purchase_price: float

    monthly_rent: float

    monthly_cash_flow: float

    cap_rate: float

    dscr: float

    score: float


class AcquisitionPortfolioBridge:
    """
    Converts acquisition decisions into portfolio assets.
    """

    @staticmethod
    def convert(
        result: AcquisitionResult,
    ) -> PortfolioAsset:
        """
        Convert acquisition result into portfolio asset.
        """

        opportunity = result.opportunity

        return PortfolioAsset(
            address=opportunity.address,
            purchase_price=opportunity.purchase_price,
            monthly_rent=opportunity.monthly_rent,
            monthly_cash_flow=(opportunity.monthly_rent - opportunity.monthly_expenses),
            cap_rate=getattr(
                result.analysis,
                "cap_rate",
                0.0,
            ),
            dscr=getattr(
                result.analysis,
                "dscr",
                0.0,
            ),
            score=result.score,
        )

    @staticmethod
    def add_to_portfolio(
        portfolio: Portfolio,
        result: AcquisitionResult,
    ) -> PortfolioAsset:
        """
        Add approved acquisition to portfolio.
        """

        asset = AcquisitionPortfolioBridge.convert(
            result,
        )

        portfolio.add_asset(
            asset,
        )

        return asset
