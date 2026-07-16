"""
File reader tests.
"""

import json

from meridianforge.imports.file_reader import (
    FileReader,
)


def test_csv_file_reader(tmp_path) -> None:
    """
    Verify CSV files load correctly.
    """

    file = tmp_path / "properties.csv"

    file.write_text(
        "Price,Rent\n250000,2200\n",
    )

    result = FileReader.read(
        str(file),
    )

    assert result.rows_loaded == 1
    assert result.records[0]["Price"] == "250000"


def test_json_file_reader(tmp_path) -> None:
    """
    Verify JSON files load correctly.
    """

    file = tmp_path / "properties.json"

    file.write_text(
        json.dumps(
            [
                {
                    "price": 250000,
                    "rent": 2200,
                }
            ]
        )
    )

    result = FileReader.read(
        str(file),
    )

    assert result.rows_loaded == 1
    assert result.records[0]["price"] == 250000


def test_unsupported_file_type(tmp_path) -> None:
    """
    Verify unsupported files return warnings.
    """

    file = tmp_path / "properties.xlsx"

    file.write_text(
        "placeholder",
    )

    result = FileReader.read(
        str(file),
    )

    assert result.rows_loaded == 0
    assert len(result.warnings) == 1
