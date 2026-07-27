"""
Opportunity Inbox service.

SP-410

Receives artifacts, assigns tracking information,
detects duplicates and stores accepted records.
"""

from __future__ import annotations

from meridianforge.opportunity.duplicate_detector import (
    DuplicateDetector,
)
from meridianforge.opportunity.inbox_record import (
    OpportunityInboxRecord,
)
from meridianforge.opportunity.inbox_status import (
    OpportunityInboxStatus,
)
from meridianforge.repositories.opportunity_repository import (
    OpportunityRepository,
)


class OpportunityInboxService:
    """
    Coordinates Opportunity Inbox processing.
    """

    def __init__(
        self,
        repository: OpportunityRepository | None = None,
    ) -> None:
        self._repository = repository or OpportunityRepository()

    def receive(
        self,
        *,
        source: str,
        source_reference: str,
        metadata: dict[str, str] | None = None,
    ) -> OpportunityInboxRecord:
        """
        Receive an artifact into the inbox.
        """

        fingerprint = DuplicateDetector.fingerprint(
            source=source,
            source_reference=source_reference,
        )

        record = OpportunityInboxRecord(
            source=source,
            source_reference=source_reference,
            duplicate_hash=fingerprint,
            metadata=metadata or {},
        )

        existing = self._repository.get_all()

        if DuplicateDetector.is_duplicate(
            record,
            existing,
        ):
            record.status = OpportunityInboxStatus.DUPLICATE
            return record

        record.status = OpportunityInboxStatus.READY

        self._repository.add(
            record,
        )

        return record
