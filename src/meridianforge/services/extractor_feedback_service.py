"""
Extractor feedback service.

MF-440.6.1

Stores and summarizes extractor decision outcomes.
"""

from __future__ import annotations

from meridianforge.models.domain.extractor_feedback_record import (
    ExtractorFeedbackRecord,
)


class ExtractorFeedbackService:
    """
    Manage extractor decision feedback records.
    """

    def __init__(self) -> None:
        self._records: list[ExtractorFeedbackRecord] = []

    def record(
        self,
        feedback: ExtractorFeedbackRecord,
    ) -> None:
        """
        Store extractor feedback.
        """

        self._records.append(
            feedback,
        )

    def all(
        self,
    ) -> list[ExtractorFeedbackRecord]:
        """
        Return recorded feedback.
        """

        return list(self._records)

    def count(
        self,
    ) -> int:
        """
        Return feedback count.
        """

        return len(self._records)
