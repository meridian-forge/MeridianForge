from pathlib import Path

from meridianforge.operations.report_archive import (
    ReportArchiveService,
)


def test_report_archive_creates_archive(tmp_path: Path):

    report_file = tmp_path / "investor_review.md"

    report_file.write_text(
        "# Meridian Forge",
        encoding="utf-8",
    )

    archive_root = tmp_path / "archive"

    result = ReportArchiveService().archive(
        files=[
            report_file,
        ],
        metadata={
            "recommendation": "BUY",
            "confidence": 0.91,
        },
        archive_root=archive_root,
    )

    assert result.exists()

    assert (result / "investor_review.md").exists()

    assert (result / "metadata.json").exists()
