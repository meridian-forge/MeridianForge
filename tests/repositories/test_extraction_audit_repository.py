from meridianforge.models.domain.extraction_audit import (
    ExtractionAuditRecord,
    ExtractionAuditStatus,
)
from meridianforge.repositories.extraction_audit_repository import (
    ExtractionAuditRepository,
)


def _record(
    artifact: str,
    field: str,
    status: ExtractionAuditStatus,
) -> ExtractionAuditRecord:
    return ExtractionAuditRecord(
        artifact_id=artifact,
        source_file="deal.pdf",
        field_name=field,
        raw_value="100000",
        normalized_value="100000",
        confidence=0.95,
        extractor="RentalAcquisitionExtractor",
        status=status,
    )


def test_repository_save_and_query() -> None:
    repo = ExtractionAuditRepository()

    first = _record(
        "A1",
        "purchase_price",
        ExtractionAuditStatus.ACCEPTED,
    )

    second = _record(
        "A1",
        "monthly_rent",
        ExtractionAuditStatus.REVIEW,
    )

    third = _record(
        "A2",
        "purchase_price",
        ExtractionAuditStatus.ACCEPTED,
    )

    repo.save(first)
    repo.save(second)
    repo.save(third)

    assert repo.count() == 3
    assert len(repo.by_artifact("A1")) == 2
    assert len(repo.by_field("purchase_price")) == 2
    assert len(repo.by_status(ExtractionAuditStatus.ACCEPTED)) == 2
    assert len(repo.by_status(ExtractionAuditStatus.REVIEW)) == 1
