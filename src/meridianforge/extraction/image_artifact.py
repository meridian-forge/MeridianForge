"""
Image artifact models.

Represents visual assets discovered inside investment artifacts.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class ImageArtifact:
    """
    Image discovered inside a source artifact.
    """

    source_file: Path
    sheet_name: str | None
    image_index: int
    image_path: Path
