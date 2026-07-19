from pathlib import Path

from meridianforge.reporting.investor_report import (
    InvestorReport,
)


class ReportExporter:
    """
    Exports Meridian Forge reports to files.
    """

    def export_markdown(
        self,
        report: InvestorReport,
        output_path: Path,
    ) -> Path:
        """
        Export report as Markdown.
        """

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        output_path.write_text(
            report.render(),
            encoding="utf-8",
        )

        return output_path

    def export_text(
        self,
        report: InvestorReport,
        output_path: Path,
    ) -> Path:
        """
        Export report as plain text.
        """

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        output_path.write_text(
            report.render(),
            encoding="utf-8",
        )

        return output_path
