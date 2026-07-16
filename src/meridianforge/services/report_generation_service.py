"""
Investment report generation service.

Transforms ranked investment results
into investor-friendly summaries.
"""

from meridianforge.models.results.investment_report import (
    InvestmentReport,
)
from meridianforge.models.results.ranked_deal import (
    RankedDeal,
)


class ReportGenerationService:
    """
    Creates investment decision reports.
    """

    @staticmethod
    def generate(
        ranked_deals: list[RankedDeal],
    ) -> InvestmentReport:
        """
        Generate investor report.
        """

        recommendations: list[str] = []

        warnings: list[str] = []

        if not ranked_deals:
            return InvestmentReport(
                title="Meridian Forge Investment Report",
                total_opportunities=0,
                summary="No investment opportunities analyzed.",
            )

        top_deal = ranked_deals[0]

        recommendations.append(
            "Review top ranked opportunity: " f"{top_deal.property.address.city}"
        )

        if top_deal.evaluation.score >= 80:
            summary = "Top opportunities show strong " "investment characteristics."
        elif top_deal.evaluation.score >= 60:
            summary = "Opportunities require additional " "review before investing."
        else:
            summary = (
                "Current opportunities do not meet " "strong investment thresholds."
            )

        for deal in ranked_deals:

            if not deal.evaluation.qualified:
                warnings.append(
                    "Property failed investor criteria: "
                    f"{deal.property.address.city}"
                )

        return InvestmentReport(
            title="Meridian Forge Investment Report",
            total_opportunities=len(ranked_deals),
            ranked_deals=ranked_deals,
            summary=summary,
            recommendations=recommendations,
            warnings=warnings,
        )
