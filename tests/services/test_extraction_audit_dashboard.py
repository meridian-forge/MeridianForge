from meridianforge.models.domain.extraction_audit import (
    ExtractionAuditRecord,
    ExtractionAuditStatus,
)
from meridianforge.repositories.extraction_audit_repository import (
    ExtractionAuditRepository,
)
from meridianforge.services.extraction_audit_dashboard import (
    ExtractionAuditDashboardService,
)


def test_dashboard_aggregates_repository_metrics() -> None:
    repository = ExtractionAuditRepository()

    repository.save(
        ExtractionAuditRecord(
            artifact_id="artifact-1",
            source_file="deal.pdf",
            field_name="purchase_price",
            raw_value="$339,000",
            normalized_value="339000",
            confidence=0.98,
            extractor="RentalAcquisitionExtractor",
            status=ExtractionAuditStatus.ACCEPTED,
        )
    )

    repository.save(
        ExtractionAuditRecord(
            artifact_id="artifact-1",
            source_file="deal.pdf",
            field_name="monthly_rent",
            raw_value="$3,135",
            normalized_value="3135",
            confidence=0.92,
            extractor="RentalAcquisitionExtractor",
            status=ExtractionAuditStatus.REVIEW,
        )
    )

    repository.save(
        ExtractionAuditRecord(
            artifact_id="artifact-2",
            source_file="other.pdf",
            field_name="roi",
            raw_value="N/A",
            normalized_value=None,
            confidence=0.20,
            extractor="RentalAcquisitionExtractor",
            status=ExtractionAuditStatus.REJECTED,
        )
    )

    dashboard = ExtractionAuditDashboardService(
        repository=repository,
    ).build_dashboard()

    assert dashboard.total_records == 3
    assert dashboard.accepted == 1
    assert dashboard.review == 1
    assert dashboard.rejected == 1
    assert round(dashboard.average_confidence, 2) == 0.70
