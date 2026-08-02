"""
Extraction audit repository.

MF-513.2.1

In-memory repository for extraction audit records. This provides a
persistence boundary between extraction workflows and future learning
components.
"""

from __future__ import annotations

from meridianforge.models.domain.extraction_audit import (
    ExtractionAuditRecord,
    ExtractionAuditStatus,
)


class ExtractionAuditRepository:
    """
    Store and query extraction audit records.

    The initial implementation is intentionally in-memory so the
    extraction audit layer can be integrated before a database or
    filesystem persistence backend is introduced.
    """

    def __init__(self) -> None:
        self._records: list[ExtractionAuditRecord] = []

    def save(
        self,
        record: ExtractionAuditRecord,
    ) -> None:
        """
        Persist a single audit record.
        """

        self._records.append(record)

    def all(self) -> list[ExtractionAuditRecord]:
        """
        Return all stored audit records.
        """

        return list(self._records)

    def by_artifact(
        self,
        artifact_id: str,
    ) -> list[ExtractionAuditRecord]:
        """
        Return all records associated with an artifact.
        """

        return [
            record
            for record in self._records
            if record.artifact_id == artifact_id
        ]

    def by_field(
        self,
        field_name: str,
    ) -> list[ExtractionAuditRecord]:
        """
        Return all records for a normalized field.
        """

        return [
            record
            for record in self._records
            if record.field_name == field_name
        ]

    def by_status(
        self,
        status: ExtractionAuditStatus,
    ) -> list[ExtractionAuditRecord]:
        """
        Return all records with the given audit status.
        """

        return [
            record
            for record in self._records
            if record.status == status
        ]

    def count(self) -> int:
        """
        Return the number of stored records.
        """

        return len(self._records)
