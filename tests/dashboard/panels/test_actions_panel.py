from meridianforge.dashboard.panels.actions import (
    ActionsPanelBuilder,
)
from meridianforge.portfolio.operations.action import (
    PortfolioAction,
)


def test_actions_panel_builds():

    panel = ActionsPanelBuilder().build(
        [
            PortfolioAction(
                action_type="REVIEW",
                description="Review asset",
                priority="HIGH",
            )
        ]
    )

    assert panel[0].priority == "HIGH"

    assert panel[0].action == "Review asset"
