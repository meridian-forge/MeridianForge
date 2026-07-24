"""
Portfolio action execution service.

MF-347.3
"""

from meridianforge.portfolio.operations.action import (
    PortfolioAction,
)
from meridianforge.portfolio.operations.action_status import (
    PortfolioActionStatus,
)


class PortfolioActionExecutor:
    """
    Executes portfolio actions.
    """

    def start(
        self,
        action: PortfolioAction,
    ) -> None:
        """
        Move action into execution.
        """

        action.status = PortfolioActionStatus.IN_PROGRESS.value

    def complete(
        self,
        action: PortfolioAction,
    ) -> None:
        """
        Complete action.
        """

        action.status = PortfolioActionStatus.COMPLETED.value
