"""
Extraction audit domain model.

MF-513.1 / MF-440.4.2

Tracks how MeridianForge transforms external artifacts
into normalized investment intelligence inputs.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum


class ExtractionAuditStatus(StrEnum):
    """
    Extraction validation states.
    """

    ACCEPTED = "accepted"
    REVIEW = "review"
    REJECTED = "rejected"
    UNKNOWN = "unknown"


@dataclass(frozen=True, slots=True)
class ExtractionAuditRecord:
    """
    Immutable record of an extracted field transformation.
    """

    artifact_id: str

    source_file: str

    field_name: str

    raw_value: str

    normalized_value: str | None

    confidence: float

    extractor: str

    status: ExtractionAuditStatus

    provider: str | None = None
