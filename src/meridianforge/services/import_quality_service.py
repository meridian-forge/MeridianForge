"""
Import quality service.

Creates user-facing summaries from
import pipeline results.
"""

from meridianforge.models.results.import_quality_report import (
    ImportQualityReport,
)
from meridianforge.models.results.pipeline_result import (
    PipelineResult,
)


class ImportQualityService:
    """
    Generates import quality reports.
    """

    @staticmethod
    def generate(
        pipeline_result: PipelineResult,
        records_received: int,
        recognized_fields: list[str] | None = None,
        unknown_fields: list[str] | None = None,
    ) -> ImportQualityReport:
        """
        Create quality report.
        """

        return ImportQualityReport(
            records_received=records_received,
            records_processed=len(pipeline_result.assets),
            confidence=pipeline_result.confidence,
            recognized_fields=(recognized_fields or []),
            unknown_fields=(unknown_fields or []),
            warnings=pipeline_result.warnings,
        )
