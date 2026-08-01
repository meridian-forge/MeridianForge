from __future__ import annotations

from pathlib import Path

from meridianforge.operations.input_adapter import (
    InputAdapter,
)


class DirectoryInputAdapter(InputAdapter):
    """
    Default filesystem adapter used by the existing Monday workflow.
    """

    def __init__(
        self,
        directory: Path,
    ) -> None:
        self.directory = directory

    def discover(self) -> list[Path]:
        if not self.directory.exists():
            return []

        return sorted([path for path in self.directory.iterdir() if path.is_file()])
