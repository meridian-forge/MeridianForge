from pathlib import Path

from meridianforge.operations.report_manager import (
    create_report_directory,
    create_report_filename,
)


def test_report_directory(
    tmp_path: Path,
) -> None:

    folder = create_report_directory(
        tmp_path
    )

    assert folder.exists()


def test_report_filename() -> None:

    filename = create_report_filename()

    assert filename.endswith(
        ".xlsx"
    )
