from meridianforge.portfolio.operations.action import (
    PortfolioAction,
)


def test_portfolio_action_completion():

    action = PortfolioAction(
        action_type="REFINANCE_REVIEW",
        description="Evaluate refinance opportunity",
        priority="HIGH",
    )

    assert action.is_open

    action.complete()

    assert action.status == "COMPLETED"
    assert not action.is_open
