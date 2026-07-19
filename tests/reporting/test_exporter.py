from pathlib import Path

from meridianforge.reporting.exporter import (
    ReportExporter,
)
from meridianforge.reporting.investor_report import (
    InvestorReport,
)


def test_markdown_export(tmp_path: Path):

    report = InvestorReport(
        title="Test Report",
        summary_lines=[
            "Meridian Forge",
            "BUY Property A",
        ],
    )

    exporter = ReportExporter()

    output = tmp_path / "brief.md"

    result = exporter.export_markdown(
        report,
        output,
    )

    assert result.exists()

    content = result.read_text()

    assert "BUY Property A" in content
