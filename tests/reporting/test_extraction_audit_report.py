from meridianforge.models.domain.extraction_audit import (
    ExtractionAuditRecord,
    ExtractionAuditStatus,
)
from meridianforge.reporting.extraction_audit_report import (
    ExtractionAuditReport,
)
from meridianforge.repositories.extraction_audit_repository import (
    ExtractionAuditRepository,
)
from meridianforge.services.extraction_audit_dashboard import (
    ExtractionAuditDashboardService,
)


def test_extraction_audit_report_generates_markdown() -> None:
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

    dashboard_service = ExtractionAuditDashboardService(
        repository=repository,
    )

    report = ExtractionAuditReport(
        dashboard_service=dashboard_service,
    ).generate()

    assert "Extraction Audit Dashboard" in report
    assert "Total Records: 1" in report
    assert "Accepted: 1" in report
