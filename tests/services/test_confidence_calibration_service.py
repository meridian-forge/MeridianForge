from meridianforge.models.domain.extraction_audit import (
    ExtractionAuditRecord,
    ExtractionAuditStatus,
)
from meridianforge.repositories.extraction_audit_repository import (
    ExtractionAuditRepository,
)
from meridianforge.services.confidence_calibration_service import (
    ConfidenceCalibrationService,
)


def test_confidence_calibration_uses_historical_success_rate() -> None:
    repository = ExtractionAuditRepository()

    repository.save(
        ExtractionAuditRecord(
            artifact_id="artifact-1",
            source_file="deal.pdf",
            field_name="purchase_price",
            raw_value="$339000",
            normalized_value="339000",
            confidence=0.95,
            extractor="RentalAcquisitionExtractor",
            status=ExtractionAuditStatus.ACCEPTED,
        )
    )

    repository.save(
        ExtractionAuditRecord(
            artifact_id="artifact-2",
            source_file="deal.pdf",
            field_name="taxes",
            raw_value="bad",
            normalized_value=None,
            confidence=0.20,
            extractor="RentalAcquisitionExtractor",
            status=ExtractionAuditStatus.REJECTED,
        )
    )

    service = ConfidenceCalibrationService(
        repository=repository,
    )

    result = service.calibrate(
        extractor="RentalAcquisitionExtractor",
        raw_confidence=0.80,
    )

    assert result.raw_confidence == 0.80
    assert result.calibrated_confidence == 0.65
