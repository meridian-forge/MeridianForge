"""
Extractor feedback record.

MF-440.6.1

Captures outcome feedback from extractor routing decisions.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ExtractorFeedbackRecord:
    """
    Outcome feedback for an extractor decision.
    """

    artifact_id: str

    provider: str | None

    opportunity_type: str

    selected_extractor: str

    extraction_status: str

    decision_confidence: float = 0.0

    final_accuracy: float = 0.0
