"""
Acquisition result model.

Represents the final output container
for property acquisition analysis.
"""

from dataclasses import dataclass, field


@dataclass(slots=True)
class AcquisitionResult:
    """
    Result from acquisition processing.
    """

    confidence: float = 0.0

    recommendation: str = "MANUAL_REVIEW"

    assets_analyzed: int = 0

    missing_fields: list[str] = field(
        default_factory=list,
    )

    warnings: list[str] = field(
        default_factory=list,
    )

    metadata: dict[str, object] = field(
        default_factory=dict,
    )

    def __post_init__(self) -> None:
        """
        Validate confidence.
        """

        if not 0.0 <= self.confidence <= 1.0:
            raise ValueError("Confidence must be between 0 and 1.")
