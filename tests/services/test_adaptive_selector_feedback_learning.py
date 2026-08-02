from meridianforge.models.domain.extractor_feedback_record import (
    ExtractorFeedbackRecord,
)
from meridianforge.services.adaptive_extractor_selector import (
    AdaptiveExtractorSelector,
)
from meridianforge.services.extractor_feedback_learning_service import (
    ExtractorFeedbackLearningService,
)


def test_selector_prefers_feedback_accuracy() -> None:
    feedback = ExtractorFeedbackLearningService()

    feedback.record(
        ExtractorFeedbackRecord(
            artifact_id="1",
            provider="JWB Capital",
            opportunity_type="rental_acquisition",
            selected_extractor="ExtractorA",
            extraction_status="accepted",
            final_accuracy=0.99,
        )
    )

    feedback.record(
        ExtractorFeedbackRecord(
            artifact_id="2",
            provider="JWB Capital",
            opportunity_type="rental_acquisition",
            selected_extractor="ExtractorB",
            extraction_status="accepted",
            final_accuracy=0.80,
        )
    )

    selector = AdaptiveExtractorSelector(
        feedback_learning_service=feedback,
    )

    assert (
        selector.select(
            [
                "ExtractorA",
                "ExtractorB",
            ],
            provider="JWB Capital",
        )
        == "ExtractorA"
    )
