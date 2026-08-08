"""
Evidence field model.

Represents extracted information with provenance and confidence.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class EvidenceField:
    """
    A normalized extracted field with traceability.
    """

    name: str
    value: object

    source_file: Path | None = None
    source_sheet: str | None = None
    source_cell: str | None = None

    source_method: str = "unknown"
    confidence: float = 0.0
