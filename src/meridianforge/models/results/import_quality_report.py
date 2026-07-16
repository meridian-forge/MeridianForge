"""
Import quality report model.

Summarizes import accuracy, confidence,
warnings, and processing results.
"""

from dataclasses import dataclass, field

from meridianforge.models.results.import_warning import (
    ImportWarning,
)


@dataclass(slots=True)
class ImportQualityReport:
    """
    Quality assessment of imported data.
    """

    records_received: int

    records_processed: int

    confidence: float

    recognized_fields: list[str] = field(
        default_factory=list,
    )

    unknown_fields: list[str] = field(
        default_factory=list,
    )

    warnings: list[ImportWarning] = field(
        default_factory=list,
    )

    def __post_init__(self) -> None:
        """
        Validate report confidence.
        """

        if not 0.0 <= self.confidence <= 1.0:
            raise ValueError("Confidence must be between 0 and 1.")
