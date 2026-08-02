"""
Extractor decision context.

MF-440.1 / MF-440.8.3

Captures routing intelligence before extraction execution.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True, slots=True)
class ExtractorDecisionContext:
    """
    Context produced during extractor selection.
    """

    opportunity_type: str

    selected_extractor: str

    candidate_extractors: list[str] = field(
        default_factory=list,
    )

    historical_confidence: float = 0.0

    provider: str | None = None

    selection_reason: str = ""

    confidence_score: float = 0.0

    learning_sources: list[str] = field(
        default_factory=list,
    )
