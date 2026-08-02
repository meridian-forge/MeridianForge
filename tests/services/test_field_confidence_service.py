from meridianforge.models.domain.extraction_audit import (
    ExtractionAuditRecord,
    ExtractionAuditStatus,
)
from meridianforge.repositories.extraction_audit_repository import (
    ExtractionAuditRepository,
)
from meridianforge.services.field_confidence_service import (
    FieldConfidenceService,
)


def test_field_confidence_service_groups_by_field() -> None:
    repository = ExtractionAuditRepository()

    repository.save(
        ExtractionAuditRecord(
            artifact_id="a1",
            source_file="deal1.pdf",
            field_name="purchase_price",
            raw_value="$300,000",
            normalized_value="300000",
            confidence=0.90,
            extractor="RentalAcquisitionExtractor",
            status=ExtractionAuditStatus.ACCEPTED,
        )
    )

    repository.save(
        ExtractionAuditRecord(
            artifact_id="a2",
            source_file="deal2.pdf",
            field_name="purchase_price",
            raw_value="$350,000",
            normalized_value="350000",
            confidence=0.98,
            extractor="RentalAcquisitionExtractor",
            status=ExtractionAuditStatus.ACCEPTED,
        )
    )

    repository.save(
        ExtractionAuditRecord(
            artifact_id="a3",
            source_file="deal3.pdf",
            field_name="monthly_rent",
            raw_value="$2,100",
            normalized_value="2100",
            confidence=0.80,
            extractor="RentalAcquisitionExtractor",
            status=ExtractionAuditStatus.REVIEW,
        )
    )

    summaries = FieldConfidenceService(
        repository=repository,
    ).summarize()

    assert len(summaries) == 2

    purchase = next(
        item for item in summaries if item.field_name == "purchase_price"
    )

    rent = next(
        item for item in summaries if item.field_name == "monthly_rent"
    )

    assert purchase.samples == 2
    assert round(purchase.average_confidence, 2) == 0.94

    assert rent.samples == 1
    assert round(rent.average_confidence, 2) == 0.80
