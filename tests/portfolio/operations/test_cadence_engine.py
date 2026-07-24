from meridianforge.portfolio.operations.cadence import (
    PortfolioCadenceEngine,
)


def test_monthly_cadence():

    engine = PortfolioCadenceEngine()

    cadence = engine.monthly()

    assert cadence.frequency == "MONTHLY"


def test_quarterly_cadence():

    engine = PortfolioCadenceEngine()

    cadence = engine.quarterly()

    assert cadence.category == "STRATEGY"
