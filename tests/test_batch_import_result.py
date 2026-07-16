"""
Batch import result tests.
"""

from meridianforge.models.results.batch_import_result import (
    BatchImportResult,
)


def test_batch_import_success_rate() -> None:
    result = BatchImportResult(
        records_received=100,
        records_processed=95,
        records_failed=5,
    )

    assert result.success_rate == 0.95


def test_empty_batch_success_rate() -> None:
    result = BatchImportResult(
        records_received=0,
        records_processed=0,
        records_failed=0,
    )

    assert result.success_rate == 0.0
