from meridianforge.analysis.result import AnalysisResult
from meridianforge.acquisition.criteria import (
    AcquisitionCriteria,
)


def calculate_score(
    result: AnalysisResult,
    criteria: AcquisitionCriteria,
) -> float:

    score = 0.0

    if result.dscr >= criteria.minimum_dscr:
        score += 35

    if result.cap_rate >= criteria.minimum_cap_rate:
        score += 35

    if (
        result.cash_on_cash_return
        >= criteria.minimum_cash_return
    ):
        score += 30

    return score
