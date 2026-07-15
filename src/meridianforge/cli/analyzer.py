"""
CLI analysis orchestration.
"""

from dataclasses import dataclass

from meridianforge.imports.property_json import PropertyJsonImporter
from meridianforge.models.results.report import InvestmentReport
from meridianforge.reporting.builder import ReportBuilder


@dataclass(frozen=True)
class CLIAnalysis:
    """
    Complete CLI analysis result.
    """

    report: InvestmentReport


class CLIAnalyzer:
    """
    Coordinates property analysis for CLI usage.
    """

    @staticmethod
    def analyze_file(
        file_path: str,
    ) -> CLIAnalysis:
        """
        Analyze a property JSON file.
        """

        property_data = PropertyJsonImporter.load(
            file_path,
        )

        report = ReportBuilder.build(
            property_data,
        )

        return CLIAnalysis(
            report=report,
        )
