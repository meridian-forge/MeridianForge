from meridianforge.acquisition.pipeline_event import (
    PipelineEvent,
)

from meridianforge.acquisition.pipeline_stage import (
    PipelineStage,
)


def test_pipeline_event_creation():

    event = PipelineEvent(
        from_stage=PipelineStage.NEW,
        to_stage=PipelineStage.REVIEW,
        note="Initial review",
    )

    assert (
        event.from_stage
        == PipelineStage.NEW
    )

    assert (
        event.to_stage
        == PipelineStage.REVIEW
    )
