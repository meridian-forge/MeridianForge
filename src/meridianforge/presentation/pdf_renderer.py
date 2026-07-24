"""
PDF investor package renderer.
"""

from pathlib import Path

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    Paragraph,
    SimpleDocTemplate,
    Spacer,
)

from meridianforge.models.results.investor_package import (
    InvestorPackage,
)


class PDFInvestorReportRenderer:
    """
    Render investor package as PDF.
    """

    def render(
        self,
        package: InvestorPackage,
        output_file: Path,
    ) -> Path:
        """
        Create investor PDF report.
        """

        document = SimpleDocTemplate(
            str(output_file),
        )

        styles = getSampleStyleSheet()

        content = []

        content.append(
            Paragraph(
                "Meridian Forge Investment Package",
                styles["Title"],
            )
        )

        content.append(
            Spacer(
                1,
                12,
            )
        )

        content.append(
            Paragraph(
                str(package.review),
                styles["BodyText"],
            )
        )

        if package.recommendation:

            content.append(
                Spacer(
                    1,
                    12,
                )
            )

            content.append(
                Paragraph(
                    f"Recommendation: {package.recommendation.action.value}",
                    styles["Heading2"],
                )
            )

            content.append(
                Paragraph(
                    f"Confidence: {package.recommendation.confidence:.0%}",
                    styles["BodyText"],
                )
            )

        document.build(
            content,
        )

        return output_file
