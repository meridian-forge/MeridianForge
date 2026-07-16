"""
Import mapping result model.

Represents how confidently an external
field was mapped into Meridian Forge.
"""

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class ImportMappingResult:
    """
    Field mapping confidence result.
    """

    source_field: str

    mapped_field: str | None

    confidence: float

    def __post_init__(self) -> None:
        """
        Validate confidence range.
        """

        if not 0.0 <= self.confidence <= 1.0:
            raise ValueError("Confidence must be between 0 and 1.")
