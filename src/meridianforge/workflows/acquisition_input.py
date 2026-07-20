"""
Acquisition workflow input model.

Represents a property opportunity entering MeridianForge.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class AcquisitionInput:
    """
    Property opportunity input.
    """

    property_address: str

    purchase_price: float

    market: str

    source: str
