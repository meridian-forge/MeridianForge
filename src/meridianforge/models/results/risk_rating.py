"""
Risk rating definitions for stress analysis.
"""

from enum import StrEnum


class RiskRating(StrEnum):
    """
    Investor-facing stress test risk classification.
    """

    SAFE = "SAFE"

    WARNING = "WARNING"

    CRITICAL = "CRITICAL"
