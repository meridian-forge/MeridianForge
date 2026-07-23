from meridianforge.acquisition.pipeline_stage import (
    PipelineStage,
)


def test_pipeline_stages():

    assert PipelineStage.NEW.value == "NEW"

    assert PipelineStage.UNDER_CONTRACT.value == "UNDER_CONTRACT"
