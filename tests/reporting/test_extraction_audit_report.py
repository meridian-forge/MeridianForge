import json
from pathlib import Path

from meridianforge.models.domain.extraction_audit import (
    ExtractionAuditRecord,
    ExtractionAuditStatus,
)
from meridianforge.reporting.extraction_audit_report import (
    ExtractionAuditReport,
)


def _record(
    field: str,
    confidence: float,
    status: ExtractionAuditStatus,
) -> ExtractionAuditRecord:
    return ExtractionAuditRecord(
        artifact_id="A1",
        source_file="deal.pdf",
        field_name=field,
        raw_value="100",
        normalized_value="100",
        confidence=confidence,
        extractor="OpportunityMapper",
        status=status,
    )


def test_export_json(
    tmp_path: Path,
) -> None:
    records = [
        _record(
            "purchase_price",
            0.99,
            ExtractionAuditStatus.ACCEPTED,
        ),
        _record(
            "monthly_rent",
            0.75,
            ExtractionAuditStatus.REVIEW,
        ),
        _record(
            "roi",
            0.20,
            ExtractionAuditStatus.REJECTED,
        ),
    ]

    output = ExtractionAuditReport.export_json(
        records,
        tmp_path / "audit.json",
    )

    payload = json.loads(output.read_text())

    assert payload["summary"]["total_fields"] == 3
    assert payload["summary"]["accepted"] == 1
    assert payload["summary"]["review"] == 1
    assert payload["summary"]["rejected"] == 1
    assert len(payload["records"]) == 3
