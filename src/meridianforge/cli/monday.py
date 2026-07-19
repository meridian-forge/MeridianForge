from pathlib import Path
from typing import Protocol

from meridianforge.reporting.exporter import (
    ReportExporter,
)


class ReportProtocol(Protocol):
    """
    Interface required by the Monday workflow.
    """

    def render(self) -> str: ...


class MondayWorkflow:
    """
    Executes the Meridian Forge Monday morning workflow.
    """

    def __init__(
        self,
        report_exporter: ReportExporter,
    ) -> None:
        self.report_exporter = report_exporter

    def run(
        self,
        report: ReportProtocol,
        output_directory: Path,
    ) -> Path:
        """
        Generate weekly investor report.
        """

        output_file = output_directory / "MeridianForge_Weekly_Brief.md"

        return self.report_exporter.export_markdown(
            report,
            output_file,
        )
