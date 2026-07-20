"""
Excel investor summary renderer.

Converts WeeklyInvestorReview into an Excel workbook.
"""

from pathlib import Path

from openpyxl import Workbook

from meridianforge.product.weekly_review import WeeklyInvestorReview


class ExcelInvestorReportRenderer:
    """
    Render investor reviews into Excel format.
    """

    def render(
        self,
        review: WeeklyInvestorReview,
        output_path: Path,
    ) -> Path:
        """
        Create investor summary workbook.
        """

        workbook = Workbook()

        worksheet = workbook.active
        worksheet.title = "Investor Review"

        worksheet.append(
            [
                "Rank",
                "Property",
                "Recommendation",
                "Confidence",
                "Strengths",
                "Risks",
            ]
        )

        for card in review.cards:
            worksheet.append(
                [
                    card.rank,
                    card.property_address,
                    card.recommendation,
                    f"{card.confidence:.0%}",
                    "; ".join(card.strengths),
                    "; ".join(card.risks),
                ]
            )

        workbook.save(output_path)

        return output_path

