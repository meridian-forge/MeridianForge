"""
Import warning model.

Represents issues detected during import processing.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class ImportWarning:
    """
    Warning generated during import.
    """

    field_name: str

    message: str

    confidence: float = 0.0

    suggested_mapping: str | None = None

    suggestion_reason: str | None = None

    def __post_init__(self) -> None:
        """
        Validate confidence score.
        """

        if not 0.0 <= self.confidence <= 1.0:
            raise ValueError("Confidence must be between 0 and 1.")
