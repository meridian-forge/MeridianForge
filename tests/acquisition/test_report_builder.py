from datetime import datetime

from meridianforge.acquisition.opportunity import (
    Opportunity,
)

from meridianforge.acquisition.pipeline import (
    AcquisitionPipeline,
)

from meridianforge.acquisition.report_builder import (
    AcquisitionReportBuilder,
)


def test_report_builder_creates_report():

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

    report = AcquisitionReportBuilder.build(result)

    assert report.property_address.startswith("123 Main")

    assert report.recommendation in [
        "BUY",
        "REVIEW",
    ]

    assert report.thesis is not None
