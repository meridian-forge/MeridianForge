from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from meridianforge.workflows.monday_execution_pipeline import (
    MondayExecutionPipeline,
)


@dataclass(slots=True)
class EmailAutomationResult:
    """
    Result of the email intake automation workflow.
    """

    processed_workbooks: int = 0
    duplicate_workbooks: int = 0
    quarantined_artifacts: int = 0
    analyses_completed: int = 0


class EmailIntakeWorkflow:
    """
    Executes the email intake workflow.

    The default behavior remains local-directory based so tests and
    existing workflows continue to operate. A Gmail-backed pipeline can
    be injected by the production Monday workflow.
    """

    WORKBOOK_SUFFIXES = {".xlsx", ".xls", ".csv"}

    def __init__(
        self,
        pipeline: MondayExecutionPipeline | None = None,
    ) -> None:
        self.pipeline = pipeline

    def execute(
        self,
        inbox_directory: Path,
    ) -> EmailAutomationResult:
        pipeline = self.pipeline or MondayExecutionPipeline(
            deals_directory=inbox_directory,
        )

        result = pipeline.execute()

        processed_workbooks = sum(
            1
            for path in result.operations.files_processed
            if path.suffix.lower() in self.WORKBOOK_SUFFIXES
        )

        quarantined_artifacts = sum(
            1
            for path in result.operations.files_processed
            if path.suffix.lower() not in self.WORKBOOK_SUFFIXES
        )

        return EmailAutomationResult(
            processed_workbooks=processed_workbooks,
            duplicate_workbooks=0,
            quarantined_artifacts=quarantined_artifacts,
            analyses_completed=result.operations.analyses_completed,
        )
