"""
Portfolio recommendation engine.

MF-344.1

Generates investor actions from portfolio analytics.
"""

from dataclasses import dataclass

from meridianforge.portfolio.analytics import (
    PortfolioAnalytics,
)


@dataclass(slots=True)
class PortfolioRecommendation:
    """
    Portfolio recommendation output.
    """

    action: str

    rationale: list[str]


class PortfolioRecommendationEngine:
    """
    Converts portfolio analytics into investor recommendations.
    """

    @staticmethod
    def analyze(
        analytics: PortfolioAnalytics,
    ) -> PortfolioRecommendation:
        """
        Generate portfolio recommendations.
        """

        rationale: list[str] = []

        if analytics.average_dscr >= 1.5:
            rationale.append(
                "Debt coverage is strong",
            )
        else:
            rationale.append(
                "Debt coverage requires review",
            )

        if analytics.average_cap_rate >= 0.07:
            rationale.append(
                "Portfolio yield profile is attractive",
            )
        else:
            rationale.append(
                "Consider improving portfolio yield",
            )

        if analytics.asset_count < 3:
            action = "ACQUIRE"
            rationale.append(
                "Portfolio scale expansion recommended",
            )

        elif analytics.portfolio_score >= 90:
            action = "OPTIMIZE"
            rationale.append(
                "Portfolio quality supports optimization",
            )

        else:
            action = "REVIEW"
            rationale.append(
                "Portfolio requires monitoring",
            )

        return PortfolioRecommendation(
            action=action,
            rationale=rationale,
        )
