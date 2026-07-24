"""
Investor dashboard action panel.

MF-349.2
"""

from dataclasses import dataclass

from meridianforge.portfolio.operations.action import (
    PortfolioAction,
)


@dataclass(slots=True)
class ActionPanelItem:
    """
    Dashboard-ready action.
    """

    priority: str

    action: str


class ActionsPanelBuilder:
    """
    Converts portfolio actions into dashboard items.
    """

    def build(
        self,
        actions: list[PortfolioAction],
    ) -> list[ActionPanelItem]:
        """
        Build action dashboard items.
        """

        return [
            ActionPanelItem(
                priority=action.priority,
                action=action.description,
            )
            for action in actions
        ]
