"""
Report formatter tests.
"""

from meridianforge.imports.property_json import PropertyJsonImporter
from meridianforge.reporting.builder import ReportBuilder
from meridianforge.reporting.formatter import ReportFormatter


def test_report_formatter() -> None:
    """
    Verify investor report formatting.
    """

    property_data = PropertyJsonImporter.load(
        "examples/sample_property.json",
    )

    report = ReportBuilder.build(
        property_data,
    )

    output = ReportFormatter.format(
        report,
    )

    assert "Meridian Forge Property Analyzer" in output
    assert "FINANCIAL SUMMARY" in output
    assert "Cap Rate" in output
    assert "DSCR" in output
    assert "RISK ASSESSMENT" in output
    assert "Recommendation" in output
