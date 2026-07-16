"""
Field mapping result model.

Represents an inferred relationship between an external
field and a Meridian Forge canonical field.
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class FieldMapping:
    """
    Represents a detected field mapping.
    """

    source_field: str

    target_field: str

    confidence: float
