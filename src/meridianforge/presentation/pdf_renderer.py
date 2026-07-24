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
from meridianforge.presentation.pdf_sections import (
    PDFSectionBuilder,
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

        sections = PDFSectionBuilder.build(
            package,
        )

        for title, body in sections:

            content.append(
                Paragraph(
                    title,
                    styles["Heading2"],
                )
            )

            content.append(
                Paragraph(
                    body.replace(
                        "\n",
                        "<br/>",
                    ),
                    styles["BodyText"],
                )
            )

            content.append(
                Spacer(
                    1,
                    12,
                )
            )

        document.build(
            content,
        )

        return output_file
