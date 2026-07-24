"""
Portfolio action queue.

MF-347.1

Manages investor operating tasks.
"""

from meridianforge.portfolio.operations.action import (
    PortfolioAction,
)


class PortfolioActionQueue:
    """
    Stores and manages portfolio actions.
    """

    def __init__(self) -> None:
        self.actions: list[PortfolioAction] = []

    def add(
        self,
        action: PortfolioAction,
    ) -> None:
        """
        Add action to queue.
        """

        self.actions.append(
            action,
        )

    def pending(
        self,
    ) -> list[PortfolioAction]:
        """
        Return open actions.
        """

        return [action for action in self.actions if action.is_open]

    @property
    def count(
        self,
    ) -> int:
        """
        Return total actions.
        """

        return len(self.actions)
