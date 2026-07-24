"""
Investor report export service.

Coordinates generation of investor-facing artifacts.
"""

from pathlib import Path

from meridianforge.presentation.excel_renderer import (
    ExcelInvestorReportRenderer,
)
from meridianforge.presentation.investor_report_renderer import (
    InvestorReportRenderer,
)
from meridianforge.presentation.markdown_renderer import (
    MarkdownInvestorReportRenderer,
)
from meridianforge.presentation.pdf_renderer import (
    PDFInvestorReportRenderer,
)
from meridianforge.product.weekly_review import WeeklyInvestorReview


class InvestorReportExportService:
    """
    Generate investor report artifacts.
    """

    def __init__(self) -> None:

        self.text_renderer = InvestorReportRenderer()
        self.markdown_renderer = MarkdownInvestorReportRenderer()
        self.excel_renderer = ExcelInvestorReportRenderer()
        self.pdf_renderer = PDFInvestorReportRenderer()

    def export(
        self,
        review: WeeklyInvestorReview,
        output_directory: Path,
    ) -> list[Path]:
        """
        Generate all supported investor outputs.
        """

        output_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        generated_files: list[Path] = []

        text_file = output_directory / "investor_review.txt"

        text_file.write_text(
            self.text_renderer.render(review),
            encoding="utf-8",
        )

        generated_files.append(text_file)

        markdown_file = output_directory / "investor_review.md"

        markdown_file.write_text(
            self.markdown_renderer.render(review),
            encoding="utf-8",
        )

        generated_files.append(markdown_file)

        excel_file = output_directory / "investor_review.xlsx"

        self.excel_renderer.render(
            review,
            excel_file,
        )

        generated_files.append(excel_file)

        pdf_file = output_directory / "investor_review.pdf"

        self.pdf_renderer.render(
            review,
            pdf_file,
        )

        return generated_files
