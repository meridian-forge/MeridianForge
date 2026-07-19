from pathlib import Path

from openpyxl import Workbook

from meridianforge.intake.excel_property_adapter import (
    ExcelPropertyAdapter,
)


def test_excel_property_adapter_loads_properties(
    tmp_path: Path,
) -> None:

    file_path = tmp_path / "properties.xlsx"

    workbook = Workbook()

    sheet = workbook.active

    sheet.append(
        [
            "name",
            "status",
            "score",
            "rent",
            "price",
        ]
    )

    sheet.append(
        [
            "Property A",
            "BUY",
            95,
            2200,
            250000,
        ]
    )

    workbook.save(file_path)

    result = ExcelPropertyAdapter().load(file_path)

    assert len(result) == 1

    assert result[0]["name"] == "Property A"

    assert result[0]["status"] == "BUY"
