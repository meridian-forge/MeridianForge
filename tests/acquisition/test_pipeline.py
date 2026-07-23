from datetime import datetime

from meridianforge.acquisition import (
    AcquisitionPipeline,
)

from meridianforge.acquisition.opportunity import (
    Opportunity,
)


def test_acquisition_pipeline():

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

    assert result.opportunity == opportunity
    assert result.recommendation in [
        "BUY",
        "REVIEW",
    ]
