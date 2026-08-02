"""
Extraction audit dashboard service.

MF-513.3.1

Builds a lightweight dashboard view from extraction audit records
so operators can review extraction quality and confidence trends.
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
class ExtractionAuditDashboard:
    """
    Dashboard summary of extraction audit activity.
    """

    total_records: int
    accepted: int
    review: int
    rejected: int
    average_confidence: float


class ExtractionAuditDashboardService:
    """
    Builds dashboard summaries from audit records.
    """

    def __init__(
        self,
        repository: ExtractionAuditRepository | None = None,
    ) -> None:
        self._repository = repository or ExtractionAuditRepository()

    def build_dashboard(self) -> ExtractionAuditDashboard:
        """
        Aggregate repository records into dashboard metrics.
        """

        records = self._repository.all()

        total = len(records)

        accepted = sum(
            1 for record in records if record.status is ExtractionAuditStatus.ACCEPTED
        )

        review = sum(
            1 for record in records if record.status is ExtractionAuditStatus.REVIEW
        )

        rejected = sum(
            1 for record in records if record.status is ExtractionAuditStatus.REJECTED
        )

        average_confidence = (
            sum(record.confidence for record in records) / total if total else 0.0
        )

        return ExtractionAuditDashboard(
            total_records=total,
            accepted=accepted,
            review=review,
            rejected=rejected,
            average_confidence=average_confidence,
        )
