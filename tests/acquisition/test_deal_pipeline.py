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

    deal.move_to(
        PipelineStage.REVIEW,
        note="Analyze financials",
    )

    assert deal.stage == PipelineStage.REVIEW

    assert len(deal.events) == 1

    assert deal.events[0].note == "Analyze financials"
