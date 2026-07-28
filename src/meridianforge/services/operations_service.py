"""
Operations orchestration service.

The OperationsService is the conductor of the MeridianForge Monday workflow.

Responsibilities:
- coordinate existing services
- track execution state
- return an operations summary

Not responsible for:
- extraction
- parsing
- underwriting
- recommendations
"""

from __future__ import annotations

from datetime import datetime
from pathlib import Path

from meridianforge.models.operations import OperationsRunResult


class OperationsService:
    """
    Coordinates the MeridianForge operational workflow.

    This initial implementation establishes the orchestration boundary.
    Existing analysis services will be connected incrementally in SP-430.2+
    """

    def __init__(
        self,
        deals_directory: Path,
    ) -> None:
        self.deals_directory = deals_directory

    def discover_files(self) -> list[Path]:
        """
        Discover supported artifacts awaiting processing.

        File analysis is intentionally not performed here.
        """

        if not self.deals_directory.exists():
            return []

        return sorted(
            [path for path in self.deals_directory.iterdir() if path.is_file()]
        )

    def execute(self) -> OperationsRunResult:
        """
        Execute the operations workflow.

        Current SP-430.1 scope:
        - create execution context
        - discover incoming artifacts
        - return execution summary

        Future SP-430 increments will add:
        - FolderAnalysisService integration
        - artifact generation
        - archive lifecycle
        """

        started_at = datetime.now()

        result = OperationsRunResult(
            started_at=started_at,
        )

        discovered = self.discover_files()

        result.files_discovered.extend(discovered)

        result.completed_at = datetime.now()

        return result
