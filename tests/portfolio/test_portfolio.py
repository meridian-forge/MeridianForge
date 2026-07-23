from meridianforge.portfolio import (
    Portfolio,
)


def test_portfolio_creation():

    portfolio = Portfolio(
        name="Core Rental Portfolio",
        strategy="Cash Flow",
    )

    assert portfolio.name == (
        "Core Rental Portfolio"
    )

    assert portfolio.strategy == (
        "Cash Flow"
    )

    assert portfolio.asset_count == 0


def test_portfolio_add_asset():

    portfolio = Portfolio(
        name="Growth Portfolio",
        strategy="Appreciation",
    )

    portfolio.add_asset(
        "property-a"
    )

    assert portfolio.asset_count == 1
    assert portfolio.assets[0] == (
        "property-a"
    )
