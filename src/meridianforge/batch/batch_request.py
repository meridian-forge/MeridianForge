"""
Batch acquisition request model.

Represents a collection of acquisition opportunities
to be processed through MeridianForge.
"""

from dataclasses import dataclass, field

from meridianforge.workflows.acquisition_input import (
    AcquisitionInput,
)


@dataclass(slots=True)
class BatchRequest:
    """
    Collection of acquisition opportunities.
    """

    opportunities: list[AcquisitionInput] = field(
        default_factory=list,
    )

    max_results: int = 10

    def __post_init__(self) -> None:
        if self.max_results <= 0:
            raise ValueError("max_results must be greater than zero.")

        if not self.opportunities:
            raise ValueError("Batch request requires at least one opportunity.")
