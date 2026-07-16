"""
Pipeline result model.

Represents the output of intelligent import processing.
"""

from dataclasses import dataclass, field

from meridianforge.models.results.import_mapping_result import (
    ImportMappingResult,
)
from meridianforge.models.results.import_warning import (
    ImportWarning,
)


@dataclass(slots=True)
class PipelineResult:
    """
    Result from the import pipeline.
    """

    assets: list[dict[str, object]] = field(
        default_factory=list,
    )

    confidence: float = 0.0

    mapping_results: list[ImportMappingResult] = field(
        default_factory=list,
    )

    warnings: list[ImportWarning] = field(
        default_factory=list,
    )

    def __post_init__(self) -> None:
        """
        Validate confidence score.
        """

        if not 0.0 <= self.confidence <= 1.0:
            raise ValueError("Confidence must be between 0 and 1.")
