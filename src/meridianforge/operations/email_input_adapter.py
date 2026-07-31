from __future__ import annotations

from pathlib import Path

from meridianforge.operations.input_adapter import (
    InputAdapter,
)


class EmailInputAdapter(InputAdapter):
    """
    Email inbox adapter for the unified operations pipeline.

    Discovers files placed in the email intake directory. Classification,
    deduplication, and quarantine remain the responsibility of
    OperationsService and the artifact lifecycle.
    """

    def __init__(
        self,
        inbox_directory: Path,
    ) -> None:
        self.inbox_directory = inbox_directory

    def discover(self) -> list[Path]:
        if not self.inbox_directory.exists():
            return []

        return sorted(
            [
                path
                for path in self.inbox_directory.iterdir()
                if path.is_file()
            ]
        )
