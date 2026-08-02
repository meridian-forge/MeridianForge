"""
Extractor feedback learning service.

MF-440.6.2

Transforms extractor decision feedback into routing intelligence.
"""

from __future__ import annotations

from collections import defaultdict

from meridianforge.models.domain.extractor_feedback_learning_profile import (
    ExtractorFeedbackLearningProfile,
)
from meridianforge.models.domain.extractor_feedback_record import (
    ExtractorFeedbackRecord,
)


class ExtractorFeedbackLearningService:
    """
    Build routing intelligence from extractor feedback.
    """

    def __init__(
        self,
    ) -> None:
        self._records: list[ExtractorFeedbackRecord] = []

    def record(
        self,
        feedback: ExtractorFeedbackRecord,
    ) -> None:
        """
        Store feedback for learning.
        """

        self._records.append(
            feedback,
        )

    def build_profiles(
        self,
    ) -> list[ExtractorFeedbackLearningProfile]:
        """
        Generate feedback learning profiles.
        """

        grouped: dict[
            tuple[str, str | None],
            list[ExtractorFeedbackRecord],
        ] = defaultdict(list)

        for record in self._records:
            grouped[
                (
                    record.selected_extractor,
                    record.provider,
                )
            ].append(record)

        profiles: list[ExtractorFeedbackLearningProfile] = []

        for (
            extractor,
            provider,
        ), records in sorted(
            grouped.items(),
            key=lambda item: (
                item[0][0],
                item[0][1] or "",
            ),
        ):
            successful = sum(1 for record in records if record.final_accuracy >= 0.90)

            failed = len(records) - successful

            profiles.append(
                ExtractorFeedbackLearningProfile(
                    extractor=extractor,
                    provider=provider,
                    total_decisions=len(records),
                    successful_decisions=successful,
                    failed_decisions=failed,
                    average_accuracy=(
                        sum(record.final_accuracy for record in records) / len(records)
                    ),
                )
            )

        return profiles
