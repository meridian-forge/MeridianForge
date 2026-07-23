from datetime import datetime

from meridianforge.acquisition.deal_factory import (
    DealFactory,
)

from meridianforge.acquisition.pipeline import (
    AcquisitionPipeline,
)

from meridianforge.acquisition.opportunity import (
    Opportunity,
)

from meridianforge.acquisition.pipeline_stage import (
    PipelineStage,
)


def test_deal_factory_creates_pipeline():

    opportunity = Opportunity(
        address="123 Main",
        city="Philadelphia",
        state="PA",
        zip_code="19143",
        purchase_price=200000,
        monthly_rent=2000,
        monthly_expenses=800,
        market="Philadelphia",
        source="test",
        created_at=datetime.now(),
    )

    result = AcquisitionPipeline().run(opportunity)

    deal = DealFactory.create(
        result,
    )

    assert deal.property_address.startswith("123 Main")

    assert deal.score == result.score

    assert deal.stage in [
        PipelineStage.REVIEW,
        PipelineStage.ANALYZING,
    ]
