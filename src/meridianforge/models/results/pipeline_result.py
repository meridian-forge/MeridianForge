"""
Pipeline result model.

Represents the output of the intelligent
import workflow.
"""

from dataclasses import dataclass, field

from .import_warning import ImportWarning


@dataclass(slots=True)
class PipelineResult:
    """
    Intelligent import outcome.
    """

    assets: list[dict[str, object]] = field(
        default_factory=list,
    )

    confidence: float = 0.0

    warnings: list[ImportWarning] = field(
        default_factory=list,
    )

    def __post_init__(self) -> None:
        if not 0 <= self.confidence <= 1:
            raise ValueError("Confidence must be between 0 and 1.")
