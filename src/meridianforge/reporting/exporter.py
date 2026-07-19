from pathlib import Path
from typing import Protocol


class RenderableReport(Protocol):
    """
    Interface required for report export.
    """

    def render(self) -> str: ...


class ReportExporter:
    """
    Exports Meridian Forge reports to files.
    """

    def export_markdown(
        self,
        report: RenderableReport,
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
        report: RenderableReport,
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
