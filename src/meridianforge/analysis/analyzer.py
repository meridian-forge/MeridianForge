from meridianforge.analysis.models import (
    AnalysisInput,
    Recommendation,
)

from meridianforge.opportunity.models import Opportunity


def analyze(
    opportunity: Opportunity,
) -> AnalysisInput:

    warnings: list[str] = []

    if not opportunity.fields:
        warnings.append("Missing financial data")

    return AnalysisInput(
        opportunity_file=opportunity.source_file,
        recommendation=Recommendation.WATCH,
        warnings=warnings,
    )
