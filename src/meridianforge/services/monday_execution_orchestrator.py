from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from meridianforge.models.operations import OperationsRunResult
from meridianforge.services.operations_service import OperationsService


@dataclass(slots=True)
class MondayExecutionResult:
    """
    Result of a complete Monday execution cycle.
    """

    operations: OperationsRunResult

    @property
    def files_processed(self) -> int:
        return len(self.operations.files_processed)

    @property
    def buy_count(self) -> int:
        return self.operations.buy_count

    @property
    def watch_count(self) -> int:
        return self.operations.watch_count

    @property
    def pass_count(self) -> int:
        return self.operations.pass_count


class MondayExecutionOrchestrator:
    """
    High-level orchestration entry point for the
    Monday Morning automation workflow.
    """

    def __init__(
        self,
        deals_directory: Path,
    ) -> None:

        self.operations = OperationsService(
            deals_directory=deals_directory,
        )

    def execute(self) -> MondayExecutionResult:
        """
        Execute the complete Monday workflow.
        """

        result = self.operations.execute()

        return MondayExecutionResult(
            operations=result,
        )
