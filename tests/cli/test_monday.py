from pathlib import Path

from meridianforge.cli.monday import (
    MondayWorkflow,
)
from meridianforge.reporting.exporter import (
    ReportExporter,
)
from meridianforge.reporting.investor_report import (
    InvestorReport,
)


def test_monday_workflow(tmp_path: Path):

    workflow = MondayWorkflow(ReportExporter())

    report = InvestorReport(
        title="Weekly Brief",
        summary_lines=[
            "Meridian Forge",
            "BUY Property A",
        ],
    )

    output = workflow.run(
        report,
        tmp_path,
    )

    assert output.exists()

    assert "BUY Property A" in output.read_text()
