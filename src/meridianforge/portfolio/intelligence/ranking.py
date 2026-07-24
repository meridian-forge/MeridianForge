"""
Portfolio intelligence ranking engine.

MF-344.2

Ranks portfolio opportunities and priorities
using portfolio intelligence outputs.
"""

from dataclasses import dataclass

from meridianforge.portfolio.analytics import (
    PortfolioAnalytics,
)


@dataclass(slots=True)
class PortfolioRanking:
    """
    Portfolio ranking output.
    """

    priority: str

    score: float

    rationale: list[str]


class PortfolioRankingEngine:
    """
    Calculates investor portfolio priority.
    """

    @staticmethod
    def rank(
        analytics: PortfolioAnalytics,
    ) -> PortfolioRanking:
        """
        Generate portfolio priority ranking.
        """

        rationale: list[str] = []

        score = 0.0

        # Cash flow strength
        if analytics.average_dscr >= 1.5:
            score += 30
            rationale.append(
                "Strong debt coverage",
            )
        else:
            rationale.append(
                "Debt coverage weakness",
            )

        # Yield strength
        if analytics.average_cap_rate >= 0.07:
            score += 30
            rationale.append(
                "Strong portfolio yield",
            )
        else:
            rationale.append(
                "Yield improvement opportunity",
            )

        # Investment quality
        score += min(
            analytics.portfolio_score * 0.4,
            40,
        )

        if score >= 85:
            priority = "HIGH"

        elif score >= 70:
            priority = "MEDIUM"

        else:
            priority = "LOW"

        return PortfolioRanking(
            priority=priority,
            score=round(
                score,
                2,
            ),
            rationale=rationale,
        )
