from meridianforge.acquisition import (
    AcquisitionResult,
)


def test_acquisition_result_creation():

    result = AcquisitionResult(
        opportunity="property",
        analysis="analysis",
        score=95,
        ranking=1,
        recommendation="BUY",
        confidence=0.90,
    )

    assert result.score == 95
    assert result.recommendation == "BUY"
