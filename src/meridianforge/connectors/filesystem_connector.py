from __future__ import annotations

import shutil
from pathlib import Path

from meridianforge.connectors.connector import (
    Connector,
)


class FilesystemConnector(Connector):
    """
    Filesystem connector.

    Synchronizes artifacts from a source directory into a MeridianForge
    working directory and returns the synchronized file paths.
    """

    def __init__(
        self,
        source_directory: Path,
    ) -> None:
        self.source_directory = source_directory

    def sync(
        self,
        destination: Path,
    ) -> list[Path]:
        destination.mkdir(
            parents=True,
            exist_ok=True,
        )

        if not self.source_directory.exists():
            return []

        synchronized: list[Path] = []

        for path in sorted(self.source_directory.iterdir()):
            if not path.is_file():
                continue

            target = destination / path.name

            if path.resolve() != target.resolve():
                shutil.copy2(
                    path,
                    target,
                )

            synchronized.append(
                target,
            )

        return synchronized
