#!/bin/bash

set -e

echo "Rebuilding BatchImportProcessor..."

cat > src/meridianforge/services/batch_import_processor.py <<'PYTHON'
"""
Batch import processor.

Processes collections of records and produces
batch intelligence results.
"""

from meridianforge.intelligence.batch_confidence import (
    BatchConfidence,
)

from meridianforge.models.results.batch_import_result import (
    BatchImportResult,
)

from meridianforge.services.import_pipeline import (
    ImportPipeline,
)


class BatchImportProcessor:
    """
    Processes batches of investment records.
    """

    def __init__(
        self,
        pipeline: ImportPipeline | None = None,
    ) -> None:
        self.pipeline = (
            pipeline
            or ImportPipeline()
        )

    def process(
        self,
        records: list[dict[str, object]],
        asset_type: str = "UNKNOWN",
    ) -> BatchImportResult:
        """
        Process a batch of records.
        """

        pipeline_result = self.pipeline.process(
            records,
            asset_type,
        )

        processed = len(
            pipeline_result.assets
        )

        failed = (
            len(records)
            -
            processed
        )

        confidence = BatchConfidence.calculate(
            [
                pipeline_result.confidence
            ],
            failed_records=failed,
            total_records=len(records),
            unknown_fields=len(
                pipeline_result.warnings
            ),
        )

        return BatchImportResult(
            records_received=len(records),
            records_processed=processed,
            records_failed=failed,
            assets=pipeline_result.assets,
            warnings=[
                str(item)
                for item in pipeline_result.warnings
            ],
            confidence=confidence,
        )
PYTHON

black src/meridianforge/services/batch_import_processor.py

echo "BatchImportProcessor rebuilt."
