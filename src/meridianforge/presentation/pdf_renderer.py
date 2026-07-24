from pathlib import Path

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
)
from reportlab.lib.styles import getSampleStyleSheet

from meridianforge.product.weekly_review import WeeklyInvestorReview


class PDFInvestorReportRenderer:
    """
    Render investor review as PDF.
    """

    def render(
        self,
        review: WeeklyInvestorReview,
        output_file: Path,
    ) -> Path:
        """
        Create PDF investor report.
        """

        document = SimpleDocTemplate(
            str(output_file),
        )

        styles = getSampleStyleSheet()

        content = []

        content.append(
            Paragraph(
                "Meridian Forge Investor Review",
                styles["Title"],
            )
        )

        content.append(
            Spacer(1, 12),
        )

        content.append(
            Paragraph(
                str(review),
                styles["BodyText"],
            )
        )

        document.build(
            content,
        )

        return output_file
