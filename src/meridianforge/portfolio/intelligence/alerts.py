"""
Portfolio intelligence alert models.

MF-348.2
"""

from dataclasses import dataclass


@dataclass(slots=True)
class PortfolioAlert:
    """
    Portfolio condition requiring attention.
    """

    category: str

    severity: str

    message: str

    recommendation: str


class PortfolioAlertFactory:
    """
    Creates standardized portfolio alerts.
    """

    @staticmethod
    def create(
        category: str,
        severity: str,
        message: str,
        recommendation: str,
    ) -> PortfolioAlert:
        """
        Build portfolio alert.
        """

        return PortfolioAlert(
            category=category,
            severity=severity,
            message=message,
            recommendation=recommendation,
        )
