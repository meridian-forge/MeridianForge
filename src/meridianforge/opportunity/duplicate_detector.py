"""
Opportunity duplicate detector.

SP-410

Provides deterministic duplicate detection for
Opportunity Inbox artifacts.
"""

from __future__ import annotations

import hashlib

from meridianforge.opportunity.inbox_record import (
    OpportunityInboxRecord,
)


class DuplicateDetector:
    """
    Computes fingerprints and checks for duplicates.
    """

    @staticmethod
    def fingerprint(
        source: str,
        source_reference: str,
    ) -> str:
        """
        Generate a stable fingerprint for an artifact.
        """

        value = f"{source.strip().lower()}|" f"{source_reference.strip().lower()}"

        return hashlib.sha256(
            value.encode("utf-8"),
        ).hexdigest()

    @staticmethod
    def is_duplicate(
        record: OpportunityInboxRecord,
        existing: list[OpportunityInboxRecord],
    ) -> bool:
        """
        Determine whether a record already exists.
        """

        return any(item.duplicate_hash == record.duplicate_hash for item in existing)
