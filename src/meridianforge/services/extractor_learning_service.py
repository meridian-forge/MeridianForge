"""
Extractor learning service.

MF-440.4 / MF-440.4.2 / MF-440.5.1

Transforms extraction audit history into reusable extractor intelligence.
Learning is scoped by extractor and provider when provider information exists.
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

        Profiles are separated by extractor and provider.
        Provider remains optional for legacy audit history.
        """

        records = self._repository.all()

        grouped: dict[tuple[str, str | None], list] = defaultdict(list)

        for record in records:
            grouped[
                (
                    record.extractor,
                    record.provider,
                )
            ].append(record)

        profiles: list[ExtractorLearningProfile] = []

        for (
            extractor,
            provider,
        ), extractor_records in sorted(
            grouped.items(),
            key=lambda item: (
                item[0][0],
                item[0][1] or "",
            ),
        ):
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
                    provider=provider,
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

    def get_profiles(
        self,
        provider: str | None = None,
    ) -> list[ExtractorLearningProfile]:
        """
        Retrieve learned extractor profiles.

        When provider is supplied, return only profiles learned
        from that provider. Legacy provider-less profiles remain
        available through provider=None.
        """

        profiles = self.build_profiles()

        if provider is None:
            return profiles

        return [profile for profile in profiles if profile.provider == provider]
