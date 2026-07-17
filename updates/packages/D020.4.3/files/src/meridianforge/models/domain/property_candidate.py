"""
Property candidate model.

Represents extracted investment information
before full underwriting.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class PropertyCandidate:
    """
    Extracted property information.
    """

    purchase_price: float = 0.0

    monthly_rent: float = 0.0

    taxes: float = 0.0

    insurance: float = 0.0

    bedrooms: int = 0

    bathrooms: float = 0.0

    location: str = ""

    confidence: float = 0.0
