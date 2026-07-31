from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from meridianforge.workflows.monday_execution_pipeline import (
    MondayExecutionPipeline,
)


@dataclass(slots=True)
class EmailAutomationResult:
    processed_workbooks: int
    duplicate_workbooks: int
    quarantined_artifacts: int
    analyses_completed: int


class EmailIntakeWorkflow:
    """
    Backward-compatible wrapper around the canonical Monday pipeline.
    """

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

        result = pipeline.execute_from_email(
            inbox_directory,
        )

        discovered_workbooks = sum(
            1
            for path in result.operations.files_discovered
            if path.suffix.lower() == ".xlsx"
        )

        quarantined = sum(
            1
            for path in result.operations.files_discovered
            if path.suffix.lower() != ".xlsx"
        )

        return EmailAutomationResult(
            processed_workbooks=discovered_workbooks,
            duplicate_workbooks=0,
            quarantined_artifacts=quarantined,
            analyses_completed=result.operations.analyses_completed,
        )
