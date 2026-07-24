"""
Investor operating dashboard.

MF-345.1

Transforms portfolio intelligence into
a recurring investor dashboard view.
"""

from dataclasses import dataclass

from meridianforge.portfolio.intelligence.package import (
    InvestorDecisionPackage,
)


@dataclass(slots=True)
class InvestorDashboard:
    """
    Investor-facing portfolio dashboard.
    """

    status: str

    health_score: float

    priority: str

    decision: str

    recommended_action: str

    urgency: str

    highlights: list[str]

    concerns: list[str]


class InvestorDashboardBuilder:
    """
    Builds investor dashboards from decision packages.
    """

    @staticmethod
    def build(
        package: InvestorDecisionPackage,
    ) -> InvestorDashboard:
        """
        Generate investor dashboard.
        """

        highlights = list(
            package.health.strengths,
        )

        concerns = list(
            package.health.risks,
        )

        if not concerns:
            concerns.append(
                "No immediate portfolio risks identified",
            )

        return InvestorDashboard(
            status=package.health.status,
            health_score=package.health.score,
            priority=package.ranking.priority,
            decision=package.decision.decision,
            recommended_action=package.action.action,
            urgency=package.action.urgency,
            highlights=highlights,
            concerns=concerns,
        )
