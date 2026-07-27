from meridianforge.opportunity.inbox_service import (
    OpportunityInboxService,
)
from meridianforge.opportunity.inbox_status import (
    OpportunityInboxStatus,
)


def test_receive_new_artifact() -> None:
    service = OpportunityInboxService()

    record = service.receive(
        source="excel",
        source_reference="deal.xlsx",
    )

    assert record.status == OpportunityInboxStatus.READY


def test_duplicate_artifact() -> None:
    service = OpportunityInboxService()

    service.receive(
        source="excel",
        source_reference="deal.xlsx",
    )

    duplicate = service.receive(
        source="excel",
        source_reference="deal.xlsx",
    )

    assert duplicate.status == OpportunityInboxStatus.DUPLICATE
