"""
Import execution service tests.
"""

from meridianforge.services.import_execution_service import (
    ImportExecutionService,
)


def test_import_execution_returns_complete_result() -> None:

    service = ImportExecutionService()

    result = service.execute(
        [
            {
                "Purchase Price": 250000,
                "Monthly Rent": 2200,
            }
        ],
        asset_type="REAL_ESTATE",
    )

    assert len(result.assets) == 1

    assert result.quality_report is not None

    assert result.quality_report.records_received == 1
