from pathlib import Path

from meridianforge.extractors.rental_acquisition_extractor import (
    RentalAcquisitionRecord,
)
from meridianforge.repositories.extraction_audit_repository import (
    ExtractionAuditRepository,
)
from meridianforge.services.extraction_audit_service import (
    ExtractionAuditService,
)
from meridianforge.services.opportunity_mapper import (
    OpportunityMapper,
)


def test_opportunity_mapper_records_audit_events() -> None:
    repository = ExtractionAuditRepository()

    audit = ExtractionAuditService(
        repository=repository,
    )

    record = RentalAcquisitionRecord(
        city="Rosharon",
        state="TX",
        price=339000,
        rent=3135,
        cash_flow=539,
        roi=8.7,
        source_file=Path("deal.pdf"),
    )

    normalized = OpportunityMapper.from_rental_record(
        record,
        audit_service=audit,
    )

    assert normalized.acquisition.purchase_price == 339000.0
    assert repository.count() == 4

    fields = {audit_record.field_name for audit_record in repository.all()}

    assert fields == {
        "purchase_price",
        "monthly_rent",
        "cash_flow",
        "roi",
    }
