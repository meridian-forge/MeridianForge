"""
Opportunity inbox lifecycle states.

MF-410

Tracks artifact intake processing state.
"""

from enum import StrEnum


class OpportunityInboxStatus(StrEnum):
    """
    Lifecycle state for incoming opportunities.
    """

    RECEIVED = "RECEIVED"

    NORMALIZED = "NORMALIZED"

    READY = "READY"

    PROCESSING = "PROCESSING"

    COMPLETED = "COMPLETED"

    FAILED = "FAILED"

    DUPLICATE = "DUPLICATE"
