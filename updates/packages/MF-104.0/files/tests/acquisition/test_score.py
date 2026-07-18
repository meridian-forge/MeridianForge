from meridianforge.acquisition.criteria import (
    AcquisitionCriteria,
)
from meridianforge.acquisition.score import (
    calculate_score,
)
from meridianforge.analysis.result import (
    AnalysisResult,
)


def test_score():

    result = AnalysisResult(
        cash_flow_monthly=300,
        cap_rate=0.06,
        cash_on_cash_return=0.10,
        dscr=1.5,
        score=0,
    )

    score = calculate_score(
        result,
        AcquisitionCriteria(),
    )

    assert score == 100
