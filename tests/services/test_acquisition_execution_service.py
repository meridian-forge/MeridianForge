from meridianforge.models.domain.investor_profile import (
    InvestorProfile,
)

from meridianforge.models.domain.investment_strategy import (
    InvestmentStrategy,
)

from meridianforge.opportunity.models import (
    Opportunity,
)

from meridianforge.services.acquisition_execution_service import (
    AcquisitionExecutionService,
)


def test_acquisition_execution_service_runs_workflow():

    opportunity = Opportunity(
        source_file="property.csv",
        fields={
            "property_address": "123 Main St",
            "purchase_price": "250000",
            "market": "Jacksonville",
            "rent": "2500",
            "noi": "18000",
        },
        confidence=0.90,
    )

    investor = InvestorProfile(
        name="Mahi",
        strategy=InvestmentStrategy.CASH_FLOW,
    )

    result = AcquisitionExecutionService().execute(
        opportunity,
        investor,
    )

    assert result.review is not None
