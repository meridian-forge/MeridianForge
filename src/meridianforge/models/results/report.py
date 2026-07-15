"""
Investor-facing investment report model.
"""

from dataclasses import dataclass

from meridianforge.models.domain.property import Property
from meridianforge.models.results.analysis_result import AnalysisResult
from meridianforge.models.results.risk_rating import RiskRating
from meridianforge.models.results.stress_result import StressResult


@dataclass(frozen=True)
class InvestmentReport:
    """
    Complete investor analysis report.
    """

    property: Property

    analysis: AnalysisResult

    stress_result: StressResult

    risk_rating: RiskRating

    recommendation: str

    summary: str
