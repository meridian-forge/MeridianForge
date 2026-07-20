from pathlib import Path

from openpyxl import Workbook

from meridianforge.services.acquisition_file_service import (
    AcquisitionFileService,
)


def test_acquisition_file_service_loads_excel(
    tmp_path: Path,
):

    file_path = tmp_path / "property.xlsx"

    workbook = Workbook()

    sheet = workbook.active

    sheet["A1"] = "purchase_price"
    sheet["B1"] = "250000"

    sheet["A2"] = "rent"
    sheet["B2"] = "2500"

    workbook.save(file_path)

    result = AcquisitionFileService().load(
        str(file_path),
    )

    assert result.source_file == "property.xlsx"
    assert result.fields["purchase_price"] == "250000"
