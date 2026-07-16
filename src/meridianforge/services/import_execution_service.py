"""
Import execution service.

Combines pipeline processing and quality reporting
into one application-level result.
"""

from meridianforge.models.results.import_execution_result import (
    ImportExecutionResult,
)
from meridianforge.services.import_pipeline import (
    ImportPipeline,
)
from meridianforge.services.import_quality_service import (
    ImportQualityService,
)


class ImportExecutionService:
    """
    Coordinates complete import execution.
    """

    def __init__(
        self,
        pipeline: ImportPipeline | None = None,
    ) -> None:

        self.pipeline = pipeline or ImportPipeline()

    def execute(
        self,
        records: list[dict[str, object]],
        asset_type: str = "UNKNOWN",
    ) -> ImportExecutionResult:
        """
        Execute complete import flow.
        """

        pipeline_result = self.pipeline.process(
            records,
            asset_type,
        )

        quality_report = ImportQualityService.generate(
            pipeline_result,
            records_received=len(records),
        )

        return ImportExecutionResult(
            assets=pipeline_result.assets,
            quality_report=quality_report,
            warnings=pipeline_result.warnings,
        )
