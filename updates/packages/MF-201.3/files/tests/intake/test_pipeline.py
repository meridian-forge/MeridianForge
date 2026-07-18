from pathlib import Path

from openpyxl import Workbook

from meridianforge.intake.pipeline import process_file
from meridianforge.opportunity.models import OpportunityType


def test_process_file(tmp_path: Path) -> None:

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

    result = process_file(file_path)

    assert (
        result.opportunity_type
        == OpportunityType.RENTAL_PROPERTY
    )
