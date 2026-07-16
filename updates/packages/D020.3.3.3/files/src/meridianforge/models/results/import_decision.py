"""
Import decision result model.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class ImportDecision:
    """
    Represents import intelligence outcome.
    """

    source: str

    asset_type: str

    confidence: float

    mappings_used: int

    warnings: int = 0
