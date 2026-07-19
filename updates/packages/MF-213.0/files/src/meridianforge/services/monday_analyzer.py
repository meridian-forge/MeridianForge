from pathlib import Path
from typing import Any, Protocol


class AnalysisPipelineProtocol(Protocol):
    def analyze(self, opportunity: Any) -> Any:
        ...


class ReportBuilderProtocol(Protocol):
    def build(self, results: list[Any]) -> Any:
        ...


class ReportExporterProtocol(Protocol):
    def export_markdown(
        self,
        report: Any,
        output_file: Path,
    ) -> Path:
        ...


class MondayAnalyzer:
    """
    Executes the Monday investment analysis workflow.
    """

    def __init__(
        self,
        analysis_pipeline: AnalysisPipelineProtocol,
        report_builder: ReportBuilderProtocol,
        report_exporter: ReportExporterProtocol,
    ) -> None:
        self.analysis_pipeline = analysis_pipeline
        self.report_builder = report_builder
        self.report_exporter = report_exporter

    def run(
        self,
        opportunities: list[Any],
        output_directory: Path,
    ) -> Path:

        results: list[Any] = []

        for opportunity in opportunities:
            results.append(
                self.analysis_pipeline.analyze(
                    opportunity
                )
            )

        report = self.report_builder.build(results)

        output_file = (
            output_directory /
            "MeridianForge_Weekly_Brief.md"
        )

        return self.report_exporter.export_markdown(
            report,
            output_file,
        )
