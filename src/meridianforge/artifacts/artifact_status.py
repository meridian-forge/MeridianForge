"""
Artifact lifecycle states.

MF-430.4
"""

from enum import StrEnum


class ArtifactStatus(StrEnum):
    """
    State machine for investment artifacts.
    """

    RECEIVED = "RECEIVED"

    VALIDATING = "VALIDATING"

    READY = "READY"

    ANALYZED = "ANALYZED"

    REJECTED = "REJECTED"

    ARCHIVED = "ARCHIVED"
