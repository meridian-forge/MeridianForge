from meridianforge.models.domain.extractor_feedback_record import (
    ExtractorFeedbackRecord,
)
from meridianforge.services.extractor_feedback_service import (
    ExtractorFeedbackService,
)


def test_feedback_service_records_decision_outcome() -> None:
    service = ExtractorFeedbackService()

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

    records = service.all()

    assert len(records) == 1
    assert records[0].provider == "JWB Capital"
    assert records[0].selected_extractor == "RentalAcquisitionExtractor"
    assert service.count() == 1
