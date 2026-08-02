"""
Adaptive extractor selection service.

MF-513.5.3 / MF-440.6.3

Selects the preferred extractor using:
- extraction learning
- historical performance
- decision feedback intelligence
"""

from __future__ import annotations

from meridianforge.services.extractor_feedback_learning_service import (
    ExtractorFeedbackLearningService,
)
from meridianforge.services.extractor_learning_service import (
    ExtractorLearningService,
)
from meridianforge.services.extractor_performance_service import (
    ExtractorPerformanceService,
)


class AdaptiveExtractorSelector:
    """
    Choose extractors using accumulated intelligence.
    """

    def __init__(
        self,
        performance_service: ExtractorPerformanceService | None = None,
        learning_service: ExtractorLearningService | None = None,
        feedback_learning_service: ExtractorFeedbackLearningService | None = None,
    ) -> None:
        self._performance_service = performance_service or ExtractorPerformanceService()

        self._learning_service = learning_service or ExtractorLearningService()

        self._feedback_learning_service = (
            feedback_learning_service or ExtractorFeedbackLearningService()
        )

    def select(
        self,
        candidates: list[str],
        provider: str | None = None,
    ) -> str | None:
        """
        Return best extractor using all available intelligence.
        """

        if not candidates:
            return None

        performances = {
            performance.extractor: performance
            for performance in self._performance_service.summarize()
        }

        learning_profiles = {
            profile.extractor: profile
            for profile in self._learning_service.get_profiles(
                provider=provider,
            )
        }

        feedback_profiles = {
            profile.extractor: profile
            for profile in self._feedback_learning_service.build_profiles()
            if profile.provider == provider
        }

        available = [
            name
            for name in candidates
            if (
                name in performances
                or name in learning_profiles
                or name in feedback_profiles
            )
        ]

        if not available:
            return candidates[0]

        def score(
            extractor: str,
        ) -> tuple[float, float, float, int]:
            learning = learning_profiles.get(
                extractor,
            )

            performance = performances.get(
                extractor,
            )

            feedback = feedback_profiles.get(
                extractor,
            )

            extraction_confidence = learning.average_confidence if learning else 0.0

            acceptance_rate = performance.acceptance_rate if performance else 0.0

            decision_accuracy = feedback.average_accuracy if feedback else 0.0

            records = (
                performance.total_records
                if performance
                else feedback.total_decisions if feedback else 0
            )

            return (
                decision_accuracy,
                extraction_confidence,
                acceptance_rate,
                records,
            )

        return max(
            available,
            key=score,
        )
