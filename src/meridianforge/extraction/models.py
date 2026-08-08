"""
Universal extraction models.

Raw extraction layer.

No provider knowledge belongs here.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class ExtractedArtifact:
    """
    Represents raw extracted information from any artifact.
    """

    source_file: Path
    artifact_type: str
    records: list[dict[str, Any]]
