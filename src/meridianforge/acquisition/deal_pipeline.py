"""
Deal pipeline model.

MF-338.2

Tracks acquisition workflow status and history.
"""

from dataclasses import dataclass, field
from datetime import datetime

from meridianforge.acquisition.pipeline_event import (
    PipelineEvent,
)

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

    events: list[PipelineEvent] = field(
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
        note: str = "",
    ) -> None:
        """
        Move deal to new workflow stage.
        """

        event = PipelineEvent(
            from_stage=self.stage,
            to_stage=stage,
            note=note,
        )

        self.events.append(
            event,
        )

        self.stage = stage

        if note:
            self.notes.append(
                note,
            )

        self.updated_at = datetime.now()
