"""
Extractor performance scoring service.

MF-513.5.2

Aggregates historical extraction audit records by extractor and produces
performance metrics that will later feed adaptive extractor routing and
confidence tuning.
"""

from __future__ import annotations

from dataclasses import dataclass

from meridianforge.models.domain.extraction_audit import (
    ExtractionAuditStatus,
)
from meridianforge.repositories.extraction_audit_repository import (
    ExtractionAuditRepository,
)


@dataclass(frozen=True, slots=True)
class ExtractorPerformance:
    """
    Performance metrics for a single extractor.
    """

    extractor: str
    total_records: int
    accepted: int
    review: int
    rejected: int
    acceptance_rate: float


class ExtractorPerformanceService:
    """
    Compute extractor-level historical performance metrics.
    """

    def __init__(
        self,
        repository: ExtractionAuditRepository | None = None,
    ) -> None:
        self._repository = repository or ExtractionAuditRepository()

    def summarize(self) -> list[ExtractorPerformance]:
        """
        Return performance metrics grouped by extractor.
        """

        records = self._repository.all()

        grouped: dict[str, list[ExtractionAuditStatus]] = {}

        for record in records:
            grouped.setdefault(
                record.extractor,
                [],
            ).append(record.status)

        summaries: list[ExtractorPerformance] = []

        for extractor in sorted(grouped):
            statuses = grouped[extractor]

            accepted = sum(
                1 for status in statuses if status is ExtractionAuditStatus.ACCEPTED
            )

            review = sum(
                1 for status in statuses if status is ExtractionAuditStatus.REVIEW
            )

            rejected = sum(
                1 for status in statuses if status is ExtractionAuditStatus.REJECTED
            )

            total = len(statuses)

            summaries.append(
                ExtractorPerformance(
                    extractor=extractor,
                    total_records=total,
                    accepted=accepted,
                    review=review,
                    rejected=rejected,
                    acceptance_rate=(accepted / total) if total else 0.0,
                )
            )

        return summaries
