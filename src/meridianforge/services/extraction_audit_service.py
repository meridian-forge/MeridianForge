"""
Extraction audit service.

MF-513.2.2 / MF-440.4.2

Creates audit records for extracted fields and persists them through
the extraction audit repository.
"""

from __future__ import annotations

from meridianforge.models.domain.extraction_audit import (
    ExtractionAuditRecord,
    ExtractionAuditStatus,
)
from meridianforge.repositories.extraction_audit_repository import (
    ExtractionAuditRepository,
)


class ExtractionAuditService:
    """
    Record extraction transformations and confidence outcomes.
    """

    def __init__(
        self,
        repository: ExtractionAuditRepository | None = None,
    ) -> None:
        self.repository = repository or ExtractionAuditRepository()

    def record_field(
        self,
        artifact_id: str,
        source_file: str,
        field_name: str,
        raw_value: str,
        normalized_value: str | None,
        confidence: float,
        extractor: str,
        provider: str | None = None,
    ) -> ExtractionAuditRecord:
        """
        Create and persist an extraction audit record.
        """

        record = ExtractionAuditRecord(
            artifact_id=artifact_id,
            source_file=source_file,
            field_name=field_name,
            raw_value=raw_value,
            normalized_value=normalized_value,
            confidence=confidence,
            extractor=extractor,
            provider=provider,
            status=self._status_from_confidence(confidence),
        )

        self.repository.save(record)

        return record

    @staticmethod
    def _status_from_confidence(
        confidence: float,
    ) -> ExtractionAuditStatus:
        """
        Convert confidence into an audit status.
        """

        if confidence >= 0.90:
            return ExtractionAuditStatus.ACCEPTED

        if confidence >= 0.60:
            return ExtractionAuditStatus.REVIEW

        return ExtractionAuditStatus.REJECTED
