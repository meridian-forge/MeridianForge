"""
Adaptive extractor selection service.

MF-513.5.3 / MF-440.8.2

Selects the preferred extractor using:
- extraction learning
- historical performance
- decision feedback intelligence
- confidence calibration

Also provides decision explanations.
"""

from __future__ import annotations

from meridianforge.models.domain.extractor_selection_explanation import (
    ExtractorSelectionExplanation,
)
from meridianforge.services.confidence_calibration_service import (
    ConfidenceCalibrationService,
)
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
        confidence_calibration_service: ConfidenceCalibrationService | None = None,
    ) -> None:
        self._performance_service = performance_service or ExtractorPerformanceService()

        self._learning_service = learning_service or ExtractorLearningService()

        self._feedback_learning_service = (
            feedback_learning_service or ExtractorFeedbackLearningService()
        )

        self._confidence_calibration_service = (
            confidence_calibration_service or ConfidenceCalibrationService()
        )

    def select(
        self,
        candidates: list[str],
        provider: str | None = None,
    ) -> str | None:
        """
        Return selected extractor name.

        Maintains backward compatibility.
        """

        explanation = self.select_with_explanation(
            candidates,
            provider=provider,
        )

        return explanation.extractor if explanation else None

    def select_with_explanation(
        self,
        candidates: list[str],
        provider: str | None = None,
    ) -> ExtractorSelectionExplanation | None:
        """
        Return extractor selection with reasoning.
        """

        if not candidates:
            return None

        (
            available,
            performances,
            learning_profiles,
            feedback_profiles,
            scores,
        ) = self._build_selection_context(
            candidates,
            provider,
        )

        if not available:
            return ExtractorSelectionExplanation(
                extractor=candidates[0],
                provider=provider,
                reason=(
                    "No historical intelligence available; "
                    "default candidate selected."
                ),
                learning_sources=[],
            )

        selected = max(
            available,
            key=lambda extractor: scores[extractor],
        )

        learning = learning_profiles.get(selected)
        performance = performances.get(selected)
        feedback = feedback_profiles.get(selected)

        calibration = self._confidence_calibration_service.calibrate(
            extractor=selected,
            raw_confidence=(learning.average_confidence if learning else 0.0),
            provider=provider,
        )

        sources: list[str] = []

        if feedback:
            sources.append("feedback")

        if learning:
            sources.append("learning")

        if calibration.sample_size:
            sources.append("calibration")

        if performance:
            sources.append("performance")

        return ExtractorSelectionExplanation(
            extractor=selected,
            provider=provider,
            decision_accuracy=(feedback.average_accuracy if feedback else 0.0),
            calibrated_confidence=calibration.calibrated_confidence,
            historical_acceptance=(performance.acceptance_rate if performance else 0.0),
            sample_size=(
                performance.total_records
                if performance
                else feedback.total_decisions if feedback else 0
            ),
            reason=(
                "Highest combined feedback accuracy, calibrated confidence, "
                "learning confidence, and historical performance."
            ),
            learning_sources=sources,
        )

    def _build_selection_context(
        self,
        candidates: list[str],
        provider: str | None,
    ) -> tuple[
        list[str],
        dict,
        dict,
        dict,
        dict[str, tuple[float, float, float, float, int]],
    ]:
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

        scores: dict[str, tuple[float, float, float, float, int]] = {}

        for extractor in available:
            learning = learning_profiles.get(extractor)
            performance = performances.get(extractor)
            feedback = feedback_profiles.get(extractor)

            calibration = self._confidence_calibration_service.calibrate(
                extractor=extractor,
                raw_confidence=(learning.average_confidence if learning else 0.0),
                provider=provider,
            )

            scores[extractor] = (
                feedback.average_accuracy if feedback else 0.0,
                calibration.calibrated_confidence,
                learning.average_confidence if learning else 0.0,
                performance.acceptance_rate if performance else 0.0,
                (
                    performance.total_records
                    if performance
                    else feedback.total_decisions if feedback else 0
                ),
            )

        return (
            available,
            performances,
            learning_profiles,
            feedback_profiles,
            scores,
        )
