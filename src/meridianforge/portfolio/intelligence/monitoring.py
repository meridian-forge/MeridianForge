"""
Portfolio monitoring intelligence engine.

MF-348.2
"""

from meridianforge.portfolio.analytics import (
    PortfolioAnalytics,
)
from meridianforge.portfolio.intelligence.alerts import (
    PortfolioAlert,
    PortfolioAlertFactory,
)


class PortfolioMonitoringEngine:
    """
    Evaluates portfolio conditions.
    """

    def analyze(
        self,
        analytics: PortfolioAnalytics,
    ) -> list[PortfolioAlert]:
        """
        Generate alerts from portfolio metrics.
        """

        alerts: list[PortfolioAlert] = []

        if analytics.average_dscr < 1.20:
            alerts.append(
                PortfolioAlertFactory.create(
                    category="DEBT",
                    severity="HIGH",
                    message="Portfolio DSCR requires attention",
                    recommendation="Review financing structure and cash flow.",
                )
            )

        if analytics.average_cap_rate < 0.05:
            alerts.append(
                PortfolioAlertFactory.create(
                    category="RETURN",
                    severity="MEDIUM",
                    message="Portfolio yield below target",
                    recommendation="Evaluate optimization opportunities.",
                )
            )

        if analytics.portfolio_score < 75:
            alerts.append(
                PortfolioAlertFactory.create(
                    category="QUALITY",
                    severity="HIGH",
                    message="Portfolio quality score requires review",
                    recommendation="Review asset allocation.",
                )
            )

        return alerts
