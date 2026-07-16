"""
Unified file reader tests.
"""

from pathlib import Path

import pytest

from meridianforge.importers.file_reader import (
    FileReader,
)


def test_csv_reader(tmp_path: Path) -> None:
    file = tmp_path / "test.csv"

    file.write_text(
        "Price,Rent\n250000,2200\n",
        encoding="utf-8",
    )

    records = FileReader.read(
        str(file),
    )

    assert len(records) == 1
    assert records[0]["Price"] == "250000"


def test_unsupported_file() -> None:
    with pytest.raises(ValueError):
        FileReader.read(
            "test.pdf",
        )
