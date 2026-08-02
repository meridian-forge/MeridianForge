"""
Extractor feedback learning profile.

MF-440.6.2

Represents learned routing accuracy from extractor decision outcomes.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ExtractorFeedbackLearningProfile:
    """
    Learned routing quality for an extractor.
    """

    extractor: str

    provider: str | None = None

    total_decisions: int = 0

    successful_decisions: int = 0

    failed_decisions: int = 0

    average_accuracy: float = 0.0
