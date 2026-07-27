from datetime import datetime

from meridianforge.models.domain.source_document import (
    SourceDocument,
)
from meridianforge.opportunity.inbox_item import (
    OpportunityInboxItem,
)
from meridianforge.opportunity.inbox_record import (
    OpportunityInboxRecord,
)
from meridianforge.opportunity.inbox_status import (
    OpportunityInboxStatus,
)


def test_inbox_item_wraps_record_and_document() -> None:
    record = OpportunityInboxRecord(
        source="manual",
        source_reference="sample.xlsx",
        duplicate_hash="abc123",
    )

    document = SourceDocument(
        source_type="FILE",
        provider="manual",
        content="example",
    )

    item = OpportunityInboxItem(
        record=record,
        document=document,
        queued_at=datetime.now(),
    )

    assert item.record_id == record.record_id
    assert item.status == OpportunityInboxStatus.RECEIVED
    assert item.document.content == "example"
