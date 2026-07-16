"""
Investment assessment result.

Represents the complete evaluation of
an investment opportunity.
"""

from dataclasses import dataclass

from meridianforge.models.results.analysis_result import (
    AnalysisResult,
)
from meridianforge.models.results.deal_evaluation import (
    DealEvaluation,
)


@dataclass(slots=True)
class InvestmentAssessmentResult:
    """
    Complete investment assessment output.
    """

    analysis: AnalysisResult

    evaluation: DealEvaluation

    asset_status: str = "NEW"

    assessment_type: str = "ACQUISITION"
