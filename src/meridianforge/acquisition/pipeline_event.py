"""
Pipeline event model.

MF-338.2

Tracks acquisition workflow history.
"""

from dataclasses import dataclass, field
from datetime import datetime

from meridianforge.acquisition.pipeline_stage import (
    PipelineStage,
)


@dataclass(slots=True)
class PipelineEvent:
    """
    Single workflow transition event.
    """

    from_stage: PipelineStage

    to_stage: PipelineStage

    note: str = ""

    created_at: datetime = field(
        default_factory=datetime.now,
    )
