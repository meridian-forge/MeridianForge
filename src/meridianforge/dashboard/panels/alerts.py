"""
Investor dashboard alerts panel.

MF-349.2
"""

from dataclasses import dataclass

from meridianforge.portfolio.intelligence.alerts import (
    PortfolioAlert,
)


@dataclass(slots=True)
class AlertPanelItem:
    """
    Dashboard-ready alert item.
    """

    severity: str

    title: str

    recommendation: str


class AlertsPanelBuilder:
    """
    Converts portfolio alerts into dashboard items.
    """

    def build(
        self,
        alerts: list[PortfolioAlert],
    ) -> list[AlertPanelItem]:
        """
        Build dashboard alert items.
        """

        return [
            AlertPanelItem(
                severity=alert.severity,
                title=alert.message,
                recommendation=alert.recommendation,
            )
            for alert in alerts
        ]
