"""
Adaptive extractor selection service.

MF-513.5.3

Selects the preferred extractor for a document type based on historical
extractor performance metrics.
"""

from __future__ import annotations

from meridianforge.services.extractor_performance_service import (
    ExtractorPerformance,
    ExtractorPerformanceService,
)


class AdaptiveExtractorSelector:
    """
    Choose extractors using historical acceptance performance.
    """

    def __init__(
        self,
        performance_service: ExtractorPerformanceService | None = None,
    ) -> None:
        self._performance_service = performance_service or ExtractorPerformanceService()

    def select(
        self,
        candidates: list[str],
    ) -> str | None:
        """
        Return the highest-performing extractor among the candidates.
        """

        performances = {
            performance.extractor: performance
            for performance in self._performance_service.summarize()
        }

        available: list[ExtractorPerformance] = [
            performances[name] for name in candidates if name in performances
        ]

        if not available:
            return candidates[0] if candidates else None

        best = max(
            available,
            key=lambda performance: (
                performance.acceptance_rate,
                performance.total_records,
            ),
        )

        return best.extractor
