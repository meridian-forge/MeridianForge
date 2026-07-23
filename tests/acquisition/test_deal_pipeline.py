from meridianforge.acquisition.deal_pipeline import (
    DealPipeline,
)

from meridianforge.acquisition.pipeline_stage import (
    PipelineStage,
)


def test_deal_pipeline_moves_stage():

    deal = DealPipeline(
        property_address="123 Main",
    )

    assert (
        deal.stage
        == PipelineStage.NEW
    )

    deal.move_to(
        PipelineStage.REVIEW
    )

    assert (
        deal.stage
        == PipelineStage.REVIEW
    )
