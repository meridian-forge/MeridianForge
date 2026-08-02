from meridianforge.models.opportunity import OpportunityType
from meridianforge.services.opportunity_router import OpportunityRouter


class ExplanationSelectorStub:
    def select_with_explanation(
        self,
        candidates: list[str],
        provider: str | None = None,
    ):
        from meridianforge.models.domain.extractor_selection_explanation import (
            ExtractorSelectionExplanation,
        )

        return ExtractorSelectionExplanation(
            extractor=candidates[0],
            provider=provider,
            calibrated_confidence=0.91,
            reason="Provider learning selected extractor",
            learning_sources=[
                "feedback",
                "calibration",
            ],
        )


def test_router_propagates_explanation() -> None:
    router = OpportunityRouter(
        selector=ExplanationSelectorStub(),
    )

    context = router.route_with_context(
        OpportunityType.RENTAL_ACQUISITION,
        provider="JWB Capital",
    )

    assert context.provider == "JWB Capital"
    assert context.confidence_score == 0.91
    assert context.selection_reason == ("Provider learning selected extractor")
    assert "feedback" in context.learning_sources
