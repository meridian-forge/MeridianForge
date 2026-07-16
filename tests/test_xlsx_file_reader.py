"""
XLSX file reader tests.
"""

from pathlib import Path

from openpyxl import Workbook

from meridianforge.importers.file_reader import (
    FileReader,
)


def test_xlsx_reader(
    tmp_path: Path,
) -> None:

    file = tmp_path / "property.xlsx"

    workbook = Workbook()

    sheet = workbook.active

    sheet.append(
        [
            "Purchase Price",
            "Rent",
        ]
    )

    sheet.append(
        [
            250000,
            2200,
        ]
    )

    workbook.save(file)

    records = FileReader.read(str(file))

    assert len(records) == 1

    assert records[0]["Purchase Price"] == 250000

    assert records[0]["Rent"] == 2200
