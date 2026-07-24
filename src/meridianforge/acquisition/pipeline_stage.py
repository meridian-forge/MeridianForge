"""
Pipeline stage definitions.

MF-338.1

Defines the canonical acquisition workflow stages.
"""

from enum import StrEnum


class PipelineStage(StrEnum):
    """
    Acquisition workflow stages.
    """

    NEW = "NEW"

    SCREENING = "SCREENING"

    ANALYZING = "ANALYZING"

    UNDERWRITING = "UNDERWRITING"

    REVIEW = "REVIEW"

    APPROVED = "APPROVED"

    OFFER = "OFFER"

    UNDER_CONTRACT = "UNDER_CONTRACT"

    CLOSED = "CLOSED"

    REJECTED = "REJECTED"
