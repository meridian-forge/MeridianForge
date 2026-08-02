"""
Field confidence aggregation service.

MF-513.5.1

Aggregates historical extraction audit records into field-level
confidence metrics that can be used by future extractor tuning
and normalization learning systems.
"""

from __future__ import annotations

from dataclasses import dataclass

from meridianforge.repositories.extraction_audit_repository import (
    ExtractionAuditRepository,
)


@dataclass(frozen=True, slots=True)
class FieldConfidence:
    """
    Aggregated confidence metrics for a normalized field.
    """

    field_name: str
    samples: int
    average_confidence: float


class FieldConfidenceService:
    """
    Compute field-level extraction confidence statistics.
    """

    def __init__(
        self,
        repository: ExtractionAuditRepository | None = None,
    ) -> None:
        self._repository = repository or ExtractionAuditRepository()

    def summarize(self) -> list[FieldConfidence]:
        """
        Return confidence metrics grouped by normalized field.
        """

        records = self._repository.all()

        grouped: dict[str, list[float]] = {}

        for record in records:
            grouped.setdefault(
                record.field_name,
                [],
            ).append(record.confidence)

        summaries: list[FieldConfidence] = []

        for field_name in sorted(grouped):
            values = grouped[field_name]

            summaries.append(
                FieldConfidence(
                    field_name=field_name,
                    samples=len(values),
                    average_confidence=sum(values) / len(values),
                )
            )

        return summaries
