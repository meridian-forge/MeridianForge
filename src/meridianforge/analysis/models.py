"""
Analysis input models.

MF-332.5

These models represent pre-underwriting
analysis inputs.

Final underwriting outputs live in:

meridianforge.models.results.analysis_result
"""

from dataclasses import dataclass, field
from enum import StrEnum


class Recommendation(StrEnum):
    BUY = "BUY"
    WATCH = "WATCH"
    REJECT = "REJECT"


@dataclass(slots=True)
class AnalysisInput:
    """
    Input object used before underwriting.

    This replaces the ambiguous legacy
    AnalysisResult name.
    """

    opportunity_file: str

    metrics: dict[str, float] = field(
        default_factory=dict,
    )

    recommendation: Recommendation = Recommendation.WATCH

    warnings: list[str] = field(
        default_factory=list,
    )
