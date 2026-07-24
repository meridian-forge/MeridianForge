"""
Portfolio action lifecycle states.

MF-347.3
"""

from enum import Enum


class PortfolioActionStatus(str, Enum):
    """
    Lifecycle states for portfolio actions.
    """

    CREATED = "CREATED"

    ASSIGNED = "ASSIGNED"

    IN_PROGRESS = "IN_PROGRESS"

    COMPLETED = "COMPLETED"

    ARCHIVED = "ARCHIVED"
