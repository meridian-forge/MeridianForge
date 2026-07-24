"""
Investor dashboard reporting.

MF-345.2

Converts investor dashboard intelligence
into exportable report format.
"""

from dataclasses import dataclass

from meridianforge.portfolio.intelligence.dashboard import (
    InvestorDashboard,
)


@dataclass(slots=True)
class InvestorDashboardReport:
    """
    Export-ready investor dashboard report.
    """

    title: str

    sections: list[str]

    def render(self) -> str:
        """
        Render report text.
        """

        return "\n".join(
            self.sections,
        )


class InvestorDashboardReportBuilder:
    """
    Builds reports from investor dashboards.
    """

    @staticmethod
    def build(
        dashboard: InvestorDashboard,
    ) -> InvestorDashboardReport:
        """
        Generate investor dashboard report.
        """

        sections: list[str] = []

        sections.append(
            "Meridian Forge Investor Dashboard",
        )

        sections.append(
            "=" * 40,
        )

        sections.append(
            f"Status: {dashboard.status}",
        )

        sections.append(
            f"Health Score: {dashboard.health_score}",
        )

        sections.append(
            f"Priority: {dashboard.priority}",
        )

        sections.append(
            f"Decision: {dashboard.decision}",
        )

        sections.append(
            f"Recommended Action: " f"{dashboard.recommended_action}",
        )

        sections.append(
            f"Urgency: {dashboard.urgency}",
        )

        sections.append(
            "",
        )

        sections.append(
            "Highlights:",
        )

        for item in dashboard.highlights:
            sections.append(
                f"- {item}",
            )

        sections.append(
            "",
        )

        sections.append(
            "Concerns:",
        )

        for item in dashboard.concerns:
            sections.append(
                f"- {item}",
            )

        return InvestorDashboardReport(
            title="Meridian Forge Investor Dashboard",
            sections=sections,
        )
