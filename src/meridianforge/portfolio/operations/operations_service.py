"""
Portfolio operations coordination service.

MF-347.3
"""

from meridianforge.portfolio.operations.action import (
    PortfolioAction,
)
from meridianforge.portfolio.operations.action_executor import (
    PortfolioActionExecutor,
)
from meridianforge.portfolio.operations.action_router import (
    PortfolioActionRouter,
)
from meridianforge.portfolio.operations.queue import (
    PortfolioActionQueue,
)


class PortfolioOperationsService:
    """
    Coordinates portfolio operating actions.
    """

    def __init__(self) -> None:

        self.queue = PortfolioActionQueue()

        self.router = PortfolioActionRouter()

        self.executor = PortfolioActionExecutor()

    def submit(
        self,
        action: PortfolioAction,
    ) -> str:
        """
        Add action and return category.
        """

        self.queue.add(
            action,
        )

        return self.router.route(
            action,
        )

    def complete(
        self,
        action: PortfolioAction,
    ) -> None:
        """
        Complete operational action.
        """

        self.executor.complete(
            action,
        )
