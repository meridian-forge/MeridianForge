"""
Opportunity inbox record.

MF-410

Tracks incoming investment opportunity artifacts
before analysis.
"""

from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4

from meridianforge.opportunity.inbox_status import (
    OpportunityInboxStatus,
)


@dataclass(slots=True)
class OpportunityInboxRecord:
    """
    Represents an opportunity entering MeridianForge.
    """

    source: str

    source_reference: str

    duplicate_hash: str

    record_id: str = field(default_factory=lambda: str(uuid4()))

    status: OpportunityInboxStatus = OpportunityInboxStatus.RECEIVED

    received_at: datetime = field(default_factory=datetime.now)

    metadata: dict[str, str] = field(default_factory=dict)
