"""
Portfolio action lifecycle states.

MF-347.3
"""

from enum import StrEnum


class PortfolioActionStatus(StrEnum):
    """
    Lifecycle states for portfolio actions.
    """

    CREATED = "CREATED"

    ASSIGNED = "ASSIGNED"

    IN_PROGRESS = "IN_PROGRESS"

    COMPLETED = "COMPLETED"

    ARCHIVED = "ARCHIVED"
