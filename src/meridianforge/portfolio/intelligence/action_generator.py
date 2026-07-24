"""
Portfolio alert action generator.

MF-348.3

Converts portfolio alerts into operational actions.
"""

from meridianforge.portfolio.intelligence.alerts import (
    PortfolioAlert,
)
from meridianforge.portfolio.operations.action import (
    PortfolioAction,
)


class PortfolioActionGenerator:
    """
    Generates operational actions from alerts.
    """

    def generate(
        self,
        alert: PortfolioAlert,
    ) -> PortfolioAction:
        """
        Convert alert into portfolio action.
        """

        return PortfolioAction(
            action_type=self._action_type(
                alert.category,
            ),
            description=alert.message,
            priority=self._priority(
                alert.severity,
            ),
        )

    def _action_type(
        self,
        category: str,
    ) -> str:
        """
        Map alert category to action type.
        """

        mapping = {
            "DEBT": "FINANCING_REVIEW",
            "RETURN": "PERFORMANCE_REVIEW",
            "QUALITY": "PORTFOLIO_REVIEW",
        }

        return mapping.get(
            category,
            "GENERAL_REVIEW",
        )

    def _priority(
        self,
        severity: str,
    ) -> str:
        """
        Map alert severity to priority.
        """

        mapping = {
            "HIGH": "HIGH",
            "MEDIUM": "MEDIUM",
            "LOW": "LOW",
        }

        return mapping.get(
            severity,
            "MEDIUM",
        )
