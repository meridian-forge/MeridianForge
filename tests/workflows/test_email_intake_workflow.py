from pathlib import Path

from meridianforge.workflows.email_intake_workflow import (
    EmailIntakeWorkflow,
)


def test_email_workflow_processes_and_quarantines_artifacts(
    tmp_path: Path,
) -> None:
    inbox = tmp_path / "runtime" / "incoming" / "email"
    inbox.mkdir(parents=True)

    workbook = inbox / "portfolio.xlsx"
    workbook.write_bytes(b"not-a-real-xlsx")

    pdf = inbox / "offering.pdf"
    pdf.write_bytes(b"%PDF")

    workflow = EmailIntakeWorkflow()

    result = workflow.execute(
        inbox,
    )

    assert result.processed_workbooks == 1
    assert result.quarantined_artifacts == 1
