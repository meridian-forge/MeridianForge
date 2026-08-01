"""
Tests for extraction audit domain model.

MF-513.1
"""

from meridianforge.models.domain.extraction_audit import (
    ExtractionAuditRecord,
    ExtractionAuditStatus,
)


def test_extraction_audit_record_creation() -> None:
    record = ExtractionAuditRecord(
        artifact_id="artifact-001",
        source_file="ros haron_property.xlsx",
        field_name="purchase_price",
        raw_value="$339,000",
        normalized_value="339000",
        confidence=0.99,
        extractor="RentalAcquisitionExtractor",
        status=ExtractionAuditStatus.ACCEPTED,
    )

    assert record.field_name == "purchase_price"
    assert record.normalized_value == "339000"
    assert record.status == ExtractionAuditStatus.ACCEPTED


def test_extraction_audit_status_values() -> None:
    assert ExtractionAuditStatus.ACCEPTED.value == "accepted"
    assert ExtractionAuditStatus.REVIEW.value == "review"
    assert ExtractionAuditStatus.REJECTED.value == "rejected"
    assert ExtractionAuditStatus.UNKNOWN.value == "unknown"
