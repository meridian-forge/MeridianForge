"""
Deal pipeline model.

MF-338.1

Tracks acquisition workflow status.
"""

from dataclasses import dataclass, field
from datetime import datetime

from meridianforge.acquisition.pipeline_stage import (
    PipelineStage,
)


@dataclass(slots=True)
class DealPipeline:
    """
    Acquisition workflow record.
    """

    property_address: str

    stage: PipelineStage = (
        PipelineStage.NEW
    )

    score: float = 0.0

    recommendation: str = ""

    notes: list[str] = field(
        default_factory=list,
    )

    created_at: datetime = field(
        default_factory=datetime.now,
    )

    updated_at: datetime = field(
        default_factory=datetime.now,
    )

    def move_to(
        self,
        stage: PipelineStage,
    ) -> None:
        """
        Update pipeline stage.
        """

        self.stage = stage

        self.updated_at = datetime.now()
