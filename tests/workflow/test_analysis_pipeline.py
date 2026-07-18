from meridianforge.workflow import AnalysisResult


def test_analysis_result_creation():
    result = AnalysisResult(
        property="property",
        underwriting_result="underwriting",
        score=85,
        recommendation="BUY",
        decision="BUY",
        confidence=0.85,
        rationale="Strong investment profile",
    )

    assert result.decision == "BUY"
    assert result.score == 85
