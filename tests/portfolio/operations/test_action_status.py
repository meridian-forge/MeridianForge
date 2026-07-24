from meridianforge.portfolio.operations.action_status import (
    PortfolioActionStatus,
)


def test_portfolio_action_status_values():

    assert PortfolioActionStatus.CREATED.value == "CREATED"

    assert PortfolioActionStatus.COMPLETED.value == "COMPLETED"
