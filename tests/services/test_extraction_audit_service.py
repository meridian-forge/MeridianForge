from meridianforge.models.domain.extraction_audit import (
    ExtractionAuditStatus,
)
from meridianforge.repositories.extraction_audit_repository import (
    ExtractionAuditRepository,
)
from meridianforge.services.extraction_audit_service import (
    ExtractionAuditService,
)


def test_record_field_persists_and_assigns_status() -> None:
    repository = ExtractionAuditRepository()

    service = ExtractionAuditService(
        repository=repository,
    )

    record = service.record_field(
        artifact_id="A1",
        source_file="deal.pdf",
        field_name="purchase_price",
        raw_value="$339,000",
        normalized_value="339000",
        confidence=0.95,
        extractor="RentalAcquisitionExtractor",
    )

    assert record.status is ExtractionAuditStatus.ACCEPTED
    assert repository.count() == 1


def test_review_status_threshold() -> None:
    service = ExtractionAuditService()

    record = service.record_field(
        artifact_id="A2",
        source_file="deal.pdf",
        field_name="monthly_rent",
        raw_value="3135",
        normalized_value="3135",
        confidence=0.72,
        extractor="RentalAcquisitionExtractor",
    )

    assert record.status is ExtractionAuditStatus.REVIEW


def test_rejected_status_threshold() -> None:
    service = ExtractionAuditService()

    record = service.record_field(
        artifact_id="A3",
        source_file="deal.pdf",
        field_name="roi",
        raw_value="??",
        normalized_value=None,
        confidence=0.20,
        extractor="RentalAcquisitionExtractor",
    )

    assert record.status is ExtractionAuditStatus.REJECTED
