"""
Opportunity domain model.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum


class OpportunityType(StrEnum):
    """
    Canonical investment opportunity categories.
    """

    PROPERTY = "property"
    PORTFOLIO = "portfolio"
    BUSINESS = "business"
    PRIVATE_LENDING = "private_lending"
    RENTAL_ACQUISITION = "rental_acquisition"
    INVENTORY_WORKBOOK = "inventory_workbook"
    SYNDICATION = "syndication"
    OTHER = "other"
    UNKNOWN = "unknown"


@dataclass(frozen=True, slots=True)
class OpportunityClassification:
    """
    Classification result produced during intake.
    """

    opportunity_type: OpportunityType
    confidence: float
    reason: str
