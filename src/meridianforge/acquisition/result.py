"""
Acquisition result model.

MF-333.1

Canonical output of the acquisition intelligence pipeline.

Combines:
- opportunity data
- underwriting analysis
- scoring
- ranking
- decision intelligence
"""

from dataclasses import dataclass, field
from typing import Any

from meridianforge.models.results.analysis_result import (
    AnalysisResult,
)


@dataclass(slots=True)
class AcquisitionResult:
    """
    Complete acquisition intelligence output.
    """

    opportunity: Any

    analysis: AnalysisResult

    score: float

    ranking: int

    recommendation: str

    confidence: float

    warnings: list[str] = field(
        default_factory=list,
    )
