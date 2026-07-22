"""
Acquisition scoring engine.

MF-332.3

Consumes canonical underwriting AnalysisResult
and evaluates acquisition criteria.
"""

from meridianforge.acquisition.criteria import (
    AcquisitionCriteria,
)

from meridianforge.models.results.analysis_result import (
    AnalysisResult,
)


def calculate_score(
    result: AnalysisResult,
    criteria: AcquisitionCriteria,
) -> float:
    """
    Calculate acquisition qualification score.

    Scoring:
    - DSCR: 35 points
    - Cap Rate: 35 points
    - Cash-on-Cash Return: 30 points
    """

    score = 0.0

    if result.dscr >= criteria.minimum_dscr:
        score += 35

    if result.cap_rate >= criteria.minimum_cap_rate:
        score += 35

    if result.cash_on_cash_return >= criteria.minimum_cash_return:
        score += 30

    return score
