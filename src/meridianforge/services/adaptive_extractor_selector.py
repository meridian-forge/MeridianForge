"""
Adaptive extractor selection service.

MF-513.5.3 / MF-440.5.2

Selects the preferred extractor using historical performance
and provider-aware learned extractor intelligence.
"""

from __future__ import annotations

from meridianforge.services.extractor_learning_service import (
    ExtractorLearningService,
)
from meridianforge.services.extractor_performance_service import (
    ExtractorPerformanceService,
)


class AdaptiveExtractorSelector:
    """
    Choose extractors using historical extraction intelligence.
    """

    def __init__(
        self,
        performance_service: ExtractorPerformanceService | None = None,
        learning_service: ExtractorLearningService | None = None,
    ) -> None:
        self._performance_service = performance_service or ExtractorPerformanceService()

        self._learning_service = learning_service or ExtractorLearningService()

    def select(
        self,
        candidates: list[str],
        provider: str | None = None,
    ) -> str | None:
        """
        Return the best extractor among candidates.

        Provider-specific learned intelligence takes priority,
        followed by historical acceptance performance.
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

        available: list[str] = [
            name
            for name in candidates
            if name in performances or name in learning_profiles
        ]

        if not available:
            return candidates[0]

        def score(
            extractor: str,
        ) -> tuple[float, float, int]:
            profile = learning_profiles.get(
                extractor,
            )

            performance = performances.get(
                extractor,
            )

            learned_confidence = profile.average_confidence if profile else 0.0

            acceptance_rate = performance.acceptance_rate if performance else 0.0

            total_records = (
                performance.total_records
                if performance
                else profile.total_records if profile else 0
            )

            return (
                learned_confidence,
                acceptance_rate,
                total_records,
            )

        return max(
            available,
            key=score,
        )
