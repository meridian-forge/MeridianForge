from pathlib import Path

from openpyxl import Workbook

from meridianforge.intake.extractors.excel import ExcelExtractor


def test_excel_extraction(tmp_path: Path) -> None:

    file_path = tmp_path / "property.xlsx"

    workbook = Workbook()
    sheet = workbook.active

    sheet.append(
        [
            "Purchase Price",
            "250000",
        ]
    )

    workbook.save(file_path)

    result = ExcelExtractor().extract(file_path)

    assert result.fields["Purchase Price"] == "250000"
