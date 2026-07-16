"""
Import warning model.

Captures issues, unknown fields,
and confidence concerns during processing.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class ImportWarning:
    """
    Warning generated during intelligent import.
    """

    field_name: str

    message: str

    confidence: float

    def __post_init__(self) -> None:
        if not 0 <= self.confidence <= 1:
            raise ValueError("Confidence must be between 0 and 1.")
