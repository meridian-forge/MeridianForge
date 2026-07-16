"""
Suggested mapping result model.

Represents an intelligent recommendation
for an unknown source field.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class SuggestedMapping:
    """
    Proposed field mapping suggestion.
    """

    source_field: str

    target_field: str

    confidence: float

    reason: str
