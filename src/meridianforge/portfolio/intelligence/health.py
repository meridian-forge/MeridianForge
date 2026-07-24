"""
Portfolio health intelligence.

MF-344.1

Evaluates portfolio condition using
existing portfolio analytics.
"""

from dataclasses import dataclass

from meridianforge.portfolio.analytics import (
    PortfolioAnalytics,
)


@dataclass(slots=True)
class PortfolioHealth:
    """
    Portfolio health assessment result.
    """

    status: str

    score: float

    strengths: list[str]

    risks: list[str]

    recommendations: list[str]


class PortfolioHealthEngine:
    """
    Converts portfolio analytics into
    investor health intelligence.
    """

    @staticmethod
    def analyze(
        analytics: PortfolioAnalytics,
    ) -> PortfolioHealth:
        """
        Evaluate portfolio health.
        """

        strengths: list[str] = []

        risks: list[str] = []

        recommendations: list[str] = []

        health_score = 100.0

        if analytics.average_dscr >= 1.5:
            strengths.append(
                "Strong debt coverage ratio",
            )
        else:
            risks.append(
                "Debt coverage below target",
            )
            health_score -= 20

        if analytics.average_cap_rate >= 0.07:
            strengths.append(
                "Attractive portfolio yield",
            )
        else:
            risks.append(
                "Yield compression detected",
            )
            health_score -= 15

        if analytics.portfolio_score >= 90:
            strengths.append(
                "High investment quality score",
            )
        elif analytics.portfolio_score < 75:
            risks.append(
                "Portfolio quality requires review",
            )
            health_score -= 20

        if analytics.asset_count >= 3:
            recommendations.append(
                "Consider portfolio optimization opportunities",
            )
        else:
            recommendations.append(
                "Evaluate additional acquisitions for scale",
            )

        if health_score >= 90:
            status = "STRONG"

        elif health_score >= 75:
            status = "STABLE"

        else:
            status = "NEEDS_ATTENTION"

        return PortfolioHealth(
            status=status,
            score=health_score,
            strengths=strengths,
            risks=risks,
            recommendations=recommendations,
        )
