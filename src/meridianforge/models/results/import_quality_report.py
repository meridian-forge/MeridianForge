"""
Import quality report model.

Summarizes import accuracy, confidence,
field mappings, warnings, and processing results.
"""

from dataclasses import dataclass, field

from meridianforge.models.results.import_mapping_result import (
    ImportMappingResult,
)
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

    mapping_results: list[ImportMappingResult] = field(
        default_factory=list,
    )

    warnings: list[ImportWarning] = field(
        default_factory=list,
    )

    @property
    def mapped_fields_count(self) -> int:
        """
        Count successfully mapped fields.
        """

        return sum(
            1 for result in self.mapping_results if result.mapped_field is not None
        )

    def __post_init__(self) -> None:
        """
        Validate report confidence.
        """

        if not 0.0 <= self.confidence <= 1.0:
            raise ValueError("Confidence must be between 0 and 1.")
