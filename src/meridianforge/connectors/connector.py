from __future__ import annotations

from pathlib import Path
from typing import Protocol


class Connector(Protocol):
    """
    External opportunity source connector.

    A connector synchronizes artifacts from an external system into a
    local MeridianForge working directory and returns the paths that
    were made available for processing.
    """

    def sync(
        self,
        destination: Path,
    ) -> list[Path]:
        """
        Synchronize artifacts into the destination directory.
        """
        ...
