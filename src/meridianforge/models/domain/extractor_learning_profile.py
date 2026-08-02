"""
Extractor learning profile.

MF-440.4

Represents learned extractor behavior from historical extraction audits.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True, slots=True)
class ExtractorLearningProfile:
    """
    Learned performance profile for an extractor.
    """

    extractor: str

    provider: str | None = None

    successful_fields: list[str] = field(
        default_factory=list,
    )

    failed_fields: list[str] = field(
        default_factory=list,
    )

    average_confidence: float = 0.0

    total_records: int = 0
