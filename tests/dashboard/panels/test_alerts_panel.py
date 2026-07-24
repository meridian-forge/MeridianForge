from meridianforge.dashboard.panels.alerts import (
    AlertsPanelBuilder,
)
from meridianforge.portfolio.intelligence.alerts import (
    PortfolioAlert,
)


def test_alert_panel_builds():

    panel = AlertsPanelBuilder().build(
        [
            PortfolioAlert(
                category="DEBT",
                severity="HIGH",
                message="DSCR review",
                recommendation="Review financing",
            )
        ]
    )

    assert panel[0].severity == "HIGH"

    assert panel[0].title == "DSCR review"
