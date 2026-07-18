from meridianforge.analysis.models import (
    AnalysisResult,
    Recommendation,
)
from meridianforge.opportunity.models import Opportunity


def analyze(
    opportunity: Opportunity,
) -> AnalysisResult:

    warnings: list[str] = []

    if not opportunity.fields:
        warnings.append("Missing financial data")

    return AnalysisResult(
        opportunity_file=opportunity.source_file,
        recommendation=Recommendation.WATCH,
        warnings=warnings,
    )
