"""
Extractor learning service.

MF-440.4

Transforms extraction audit history into reusable extractor intelligence.
"""

from __future__ import annotations

from collections import defaultdict

from meridianforge.models.domain.extraction_audit import (
    ExtractionAuditStatus,
)
from meridianforge.models.domain.extractor_learning_profile import (
    ExtractorLearningProfile,
)
from meridianforge.repositories.extraction_audit_repository import (
    ExtractionAuditRepository,
)


class ExtractorLearningService:
    """
    Build learned extractor profiles from historical audit records.
    """

    def __init__(
        self,
        repository: ExtractionAuditRepository | None = None,
    ) -> None:
        self._repository = repository or ExtractionAuditRepository()

    def build_profiles(
        self,
    ) -> list[ExtractorLearningProfile]:
        """
        Generate extractor learning profiles.
        """

        records = self._repository.all()

        grouped: dict[str, list] = defaultdict(list)

        for record in records:
            grouped[record.extractor].append(record)

        profiles: list[ExtractorLearningProfile] = []

        for extractor, extractor_records in sorted(grouped.items()):

            successful_fields: list[str] = []
            failed_fields: list[str] = []

            confidence_total = 0.0

            for record in extractor_records:
                confidence_total += record.confidence

                if record.status is ExtractionAuditStatus.ACCEPTED:
                    successful_fields.append(
                        record.field_name,
                    )

                if record.status is ExtractionAuditStatus.REJECTED:
                    failed_fields.append(
                        record.field_name,
                    )

            profiles.append(
                ExtractorLearningProfile(
                    extractor=extractor,
                    successful_fields=sorted(
                        set(successful_fields),
                    ),
                    failed_fields=sorted(
                        set(failed_fields),
                    ),
                    average_confidence=(confidence_total / len(extractor_records)),
                    total_records=len(extractor_records),
                )
            )

        return profiles
