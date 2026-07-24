"""
Weekly investor review generator.

MF-345.1

Creates recurring investor review summaries.
"""

from dataclasses import dataclass

from meridianforge.portfolio.intelligence.dashboard import (
    InvestorDashboard,
)


@dataclass(slots=True)
class WeeklyInvestorReview:
    """
    Weekly investor review artifact.
    """

    title: str

    summary: str

    action_items: list[str]

    risk_items: list[str]


class WeeklyInvestorReviewBuilder:
    """
    Creates investor review summaries.
    """

    @staticmethod
    def build(
        dashboard: InvestorDashboard,
    ) -> WeeklyInvestorReview:
        """
        Generate weekly review.
        """

        summary = (
            f"Portfolio status: {dashboard.status}. "
            f"Decision: {dashboard.decision}. "
            f"Recommended action: "
            f"{dashboard.recommended_action}."
        )

        return WeeklyInvestorReview(
            title="Meridian Forge Weekly Investor Review",
            summary=summary,
            action_items=[
                dashboard.recommended_action,
            ],
            risk_items=list(
                dashboard.concerns,
            ),
        )
