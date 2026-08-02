from meridianforge.models.domain.extractor_feedback_record import (
    ExtractorFeedbackRecord,
)
from meridianforge.services.extractor_feedback_learning_service import (
    ExtractorFeedbackLearningService,
)


def test_feedback_learning_builds_profile() -> None:
    service = ExtractorFeedbackLearningService()

    service.record(
        ExtractorFeedbackRecord(
            artifact_id="artifact-1",
            provider="JWB Capital",
            opportunity_type="rental_acquisition",
            selected_extractor="RentalAcquisitionExtractor",
            extraction_status="accepted",
            decision_confidence=0.95,
            final_accuracy=0.98,
        )
    )

    service.record(
        ExtractorFeedbackRecord(
            artifact_id="artifact-2",
            provider="JWB Capital",
            opportunity_type="rental_acquisition",
            selected_extractor="RentalAcquisitionExtractor",
            extraction_status="accepted",
            decision_confidence=0.90,
            final_accuracy=0.92,
        )
    )

    profiles = service.build_profiles()

    assert len(profiles) == 1
    assert profiles[0].extractor == "RentalAcquisitionExtractor"
    assert profiles[0].provider == "JWB Capital"
    assert profiles[0].total_decisions == 2
    assert profiles[0].successful_decisions == 2
    assert round(profiles[0].average_accuracy, 2) == 0.95
