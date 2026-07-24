from meridianforge.portfolio.operations.action import (
    PortfolioAction,
)
from meridianforge.portfolio.operations.action_executor import (
    PortfolioActionExecutor,
)


def test_executor_completes_action():

    executor = PortfolioActionExecutor()

    action = PortfolioAction(
        action_type="PORTFOLIO_REVIEW",
        description="Review portfolio",
        priority="MEDIUM",
    )

    executor.start(
        action,
    )

    assert action.status == "IN_PROGRESS"

    executor.complete(
        action,
    )

    assert action.status == "COMPLETED"
