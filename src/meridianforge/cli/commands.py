"""
CLI command implementations.
"""

from meridianforge.cli.analyzer import CLIAnalyzer
from meridianforge.reporting.formatter import ReportFormatter


def analyze_command(
    file_path: str = "examples/sample_property.json",
) -> str:
    """
    Run property analysis command.
    """

    result = CLIAnalyzer.analyze_file(
        file_path,
    )

    return ReportFormatter.format(
        result.report,
    )
