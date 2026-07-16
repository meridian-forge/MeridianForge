"""
Batch import processor tests.
"""

from meridianforge.services.batch_import_processor import (
    BatchImportProcessor,
)


def test_batch_processor_creates_result() -> None:
    processor = BatchImportProcessor()

    result = processor.process(
        [
            {
                "Price": 250000,
                "Monthly Rent": 2200,
            }
        ]
    )

    assert result.records_received == 1
    assert result.records_processed == 1
    assert result.confidence > 0
