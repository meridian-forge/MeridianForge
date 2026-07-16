"""
Import quality report tests.
"""

from meridianforge.models.results.pipeline_result import (
    PipelineResult,
)
from meridianforge.services.import_quality_service import (
    ImportQualityService,
)


def test_quality_report_creation() -> None:

    pipeline_result = PipelineResult(
        assets=[
            {
                "purchase_price": 250000,
            }
        ],
        confidence=0.90,
    )

    report = ImportQualityService.generate(
        pipeline_result,
        records_received=1,
        recognized_fields=[
            "purchase_price",
        ],
    )

    assert report.records_received == 1
    assert report.records_processed == 1
    assert report.confidence == 0.90
    assert "purchase_price" in report.recognized_fields
