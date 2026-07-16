"""
End-to-end import workflow tests.
"""

from pathlib import Path

from meridianforge.importers.file_reader import (
    FileReader,
)
from meridianforge.services.import_execution_service import (
    ImportExecutionService,
)


def test_complete_import_workflow(
    tmp_path: Path,
) -> None:

    file = tmp_path / "property.csv"

    file.write_text(
        "Purchase Price,Monthly Rent\n" "250000,2200\n",
        encoding="utf-8",
    )

    records = FileReader.read(
        str(file),
    )

    result = ImportExecutionService().execute(
        records,
        asset_type="REAL_ESTATE",
    )

    assert len(records) == 1

    assert len(result.assets) == 1

    assert result.quality_report is not None

    assert result.quality_report.records_received == 1
