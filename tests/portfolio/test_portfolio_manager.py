from meridianforge.portfolio.portfolio import (
    Portfolio,
)

from meridianforge.portfolio.portfolio_manager import (
    PortfolioManager,
)


def test_portfolio_manager_add_asset():

    portfolio = Portfolio(
        name="Core Rentals",
        strategy="Long Term Hold",
    )

    manager = PortfolioManager(
        portfolio,
    )

    asset = "Property A"

    manager.add_asset(
        asset,
    )

    assert manager.asset_count == 1
    assert asset in portfolio.assets


def test_portfolio_manager_remove_asset():

    portfolio = Portfolio(
        name="Core Rentals",
        strategy="Long Term Hold",
    )

    asset = "Property A"

    portfolio.add_asset(
        asset,
    )

    manager = PortfolioManager(
        portfolio,
    )

    manager.remove_asset(
        asset,
    )

    assert manager.asset_count == 0


def test_portfolio_manager_returns_portfolio():

    portfolio = Portfolio(
        name="Core Rentals",
        strategy="Long Term Hold",
    )

    manager = PortfolioManager(
        portfolio,
    )

    assert manager.get_portfolio() == portfolio
