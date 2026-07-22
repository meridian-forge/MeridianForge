from meridianforge.workflow import WorkflowResult


def test_analysis_result_creation() -> None:
    result = WorkflowResult(
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
