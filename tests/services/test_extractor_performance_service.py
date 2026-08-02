from meridianforge.models.domain.extraction_audit import (
    ExtractionAuditRecord,
    ExtractionAuditStatus,
)
from meridianforge.repositories.extraction_audit_repository import (
    ExtractionAuditRepository,
)
from meridianforge.services.extractor_performance_service import (
    ExtractorPerformanceService,
)


def test_extractor_performance_service_groups_by_extractor() -> None:
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
            field_name="monthly_rent",
            raw_value="$2,100",
            normalized_value="2100",
            confidence=0.80,
            extractor="RentalAcquisitionExtractor",
            status=ExtractionAuditStatus.REVIEW,
        )
    )

    repository.save(
        ExtractionAuditRecord(
            artifact_id="a3",
            source_file="deal3.pdf",
            field_name="roi",
            raw_value="8.7%",
            normalized_value="8.7",
            confidence=0.95,
            extractor="AlternativeExtractor",
            status=ExtractionAuditStatus.ACCEPTED,
        )
    )

    summaries = ExtractorPerformanceService(
        repository=repository,
    ).summarize()

    assert len(summaries) == 2

    rental = next(
        item
        for item in summaries
        if item.extractor == "RentalAcquisitionExtractor"
    )

    alternative = next(
        item
        for item in summaries
        if item.extractor == "AlternativeExtractor"
    )

    assert rental.total_records == 2
    assert rental.accepted == 1
    assert rental.review == 1
    assert rental.rejected == 0
    assert round(rental.acceptance_rate, 2) == 0.50

    assert alternative.total_records == 1
    assert alternative.accepted == 1
    assert round(alternative.acceptance_rate, 2) == 1.00
