"""
Evidence field models.

Represents extracted facts before MeridianForge validation.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class EvidenceField:
    """
    A field extracted from an external artifact.

    This is a source claim, not a validated investment metric.
    """

    name: str
    value: object
    confidence: float
    method: str


@dataclass(frozen=True, slots=True)
class EvidenceRecord:
    """
    Collection of extracted evidence from one artifact.
    """

    source_file: Path
    fields: tuple[EvidenceField, ...]
    confidence: float
