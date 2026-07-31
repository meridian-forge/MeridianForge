from __future__ import annotations

from pathlib import Path
from typing import Protocol


class InputAdapter(Protocol):
    """
    Source adapter for MeridianForge operational inputs.
    """

    def discover(self) -> list[Path]:
        """
        Discover input artifacts for the operations pipeline.
        """
        ...
