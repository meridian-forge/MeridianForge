"""
Opportunity Inbox Item.

SP-410.2

Represents a queued artifact awaiting
normalization and analysis.

The InboxItem intentionally contains no
business logic. It bridges the Opportunity
Inbox with the existing extraction pipeline.
"""

from dataclasses import dataclass
from datetime import datetime

from meridianforge.models.domain.source_document import (
    SourceDocument,
)
from meridianforge.opportunity.inbox_record import (
    OpportunityInboxRecord,
)


@dataclass(slots=True)
class OpportunityInboxItem:
    """
    Queue item awaiting processing.
    """

    record: OpportunityInboxRecord

    document: SourceDocument

    queued_at: datetime

    @property
    def record_id(self) -> str:
        """
        Convenience access to the inbox record id.
        """

        return self.record.record_id

    @property
    def status(self):
        """
        Current inbox processing state.
        """

        return self.record.status
