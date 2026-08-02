"""
Extractor selection explanation.

MF-440.8.2

Represents the reasoning behind an adaptive extractor decision.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True, slots=True)
class ExtractorSelectionExplanation:
    """
    Explain why an extractor was selected.
    """

    extractor: str

    provider: str | None = None

    decision_accuracy: float = 0.0

    calibrated_confidence: float = 0.0

    historical_acceptance: float = 0.0

    sample_size: int = 0

    reason: str = ""

    learning_sources: list[str] = field(
        default_factory=list,
    )
