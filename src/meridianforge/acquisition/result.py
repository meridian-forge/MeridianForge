"""
Acquisition result model.

MF-335.3

Canonical output of the acquisition intelligence pipeline.

Combines:
- opportunity data
- underwriting analysis
- scoring
- ranking
- decision intelligence
- investment thesis
"""

from dataclasses import dataclass, field

from meridianforge.acquisition.opportunity import (
    Opportunity,
)

from meridianforge.acquisition.thesis import (
    InvestmentThesis,
)

from meridianforge.models.results.analysis_result import (
    AnalysisResult,
)


@dataclass(slots=True)
class AcquisitionResult:
    """
    Complete acquisition intelligence output.
    """

    opportunity: Opportunity

    analysis: AnalysisResult

    score: float

    ranking: int

    recommendation: str

    confidence: float

    thesis: InvestmentThesis | None = None

    warnings: list[str] = field(
        default_factory=list,
    )
