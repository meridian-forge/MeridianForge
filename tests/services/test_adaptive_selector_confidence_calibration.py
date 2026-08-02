from meridianforge.models.domain.extraction_audit import (
    ExtractionAuditRecord,
    ExtractionAuditStatus,
)
from meridianforge.repositories.extraction_audit_repository import (
    ExtractionAuditRepository,
)
from meridianforge.services.adaptive_extractor_selector import (
    AdaptiveExtractorSelector,
)
from meridianforge.services.confidence_calibration_service import (
    ConfidenceCalibrationService,
)


def test_selector_uses_calibrated_confidence() -> None:
    repository = ExtractionAuditRepository()

    repository.save(
        ExtractionAuditRecord(
            artifact_id="1",
            source_file="deal.pdf",
            field_name="price",
            raw_value="$300000",
            normalized_value="300000",
            confidence=0.95,
            extractor="ExtractorA",
            provider="JWB Capital",
            status=ExtractionAuditStatus.ACCEPTED,
        )
    )

    repository.save(
        ExtractionAuditRecord(
            artifact_id="2",
            source_file="deal.pdf",
            field_name="price",
            raw_value="$300000",
            normalized_value="300000",
            confidence=0.40,
            extractor="ExtractorB",
            provider="JWB Capital",
            status=ExtractionAuditStatus.REJECTED,
        )
    )

    selector = AdaptiveExtractorSelector(
        confidence_calibration_service=ConfidenceCalibrationService(
            repository=repository,
        ),
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
