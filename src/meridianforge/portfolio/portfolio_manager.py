"""
Portfolio manager service.

MF-341.3

Provides portfolio-level operations:
- add assets
- remove assets
- retrieve portfolio state
- calculate portfolio counts
"""

from meridianforge.portfolio.portfolio import (
    Portfolio,
)


class PortfolioManager:
    """
    Service responsible for portfolio operations.
    """

    def __init__(
        self,
        portfolio: Portfolio,
    ) -> None:
        """
        Initialize portfolio manager.
        """

        self.portfolio = portfolio

    def add_asset(
        self,
        asset: object,
    ) -> None:
        """
        Add an asset to the portfolio.
        """

        self.portfolio.add_asset(
            asset,
        )

    def remove_asset(
        self,
        asset: object,
    ) -> None:
        """
        Remove an asset from the portfolio.

        Silently ignores assets not present.
        """

        if asset in self.portfolio.assets:
            self.portfolio.assets.remove(
                asset,
            )

    @property
    def asset_count(
        self,
    ) -> int:
        """
        Return number of portfolio assets.
        """

        return self.portfolio.asset_count

    def get_portfolio(
        self,
    ) -> Portfolio:
        """
        Return managed portfolio.
        """

        return self.portfolio
