from pathlib import Path

from meridianforge.intake.email_intake_router import EmailIntakeRouter


def test_email_router_processes_workbooks_and_skips_other_artifacts(
    tmp_path: Path,
) -> None:
    inbox = tmp_path / "runtime" / "incoming" / "email"
    inbox.mkdir(parents=True)

    workbook = inbox / "portfolio.xlsx"
    workbook.write_bytes(b"not-a-real-xlsx")

    pdf = inbox / "offering.pdf"
    pdf.write_bytes(b"%PDF")

    router = EmailIntakeRouter()

    result = router.route(
        inbox,
    )

    assert result.processed_count == 1
    assert workbook in result.processed_workbooks
    assert pdf in result.skipped_artifacts
