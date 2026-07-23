"""
Deal pipeline stages.

MF-338.1
"""

from enum import Enum


class PipelineStage(str, Enum):
    """
    Acquisition workflow stages.
    """

    NEW = "NEW"

    ANALYZING = "ANALYZING"

    RANKED = "RANKED"

    REVIEW = "REVIEW"

    OFFER = "OFFER"

    UNDER_CONTRACT = "UNDER_CONTRACT"

    CLOSED = "CLOSED"

    REJECTED = "REJECTED"
