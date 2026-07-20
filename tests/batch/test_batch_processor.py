from meridianforge.batch.batch_processor import (
    BatchProcessor,
)
from meridianforge.batch.batch_request import (
    BatchRequest,
)
from meridianforge.product.weekly_review import (
    WeeklyInvestorReview,
)
from meridianforge.workflows.acquisition_input import (
    AcquisitionInput,
)


class FakeDecisionWorkflow:

    def execute(self, opportunity):

        return WeeklyInvestorReview()


def test_batch_processor_processes_multiple_opportunities():

    request = BatchRequest(
        opportunities=[
            AcquisitionInput(
                property_address="123 Main St",
                purchase_price=250000,
                market="Jacksonville",
                source="Zillow",
            ),
            AcquisitionInput(
                property_address="456 Oak Ave",
                purchase_price=300000,
                market="Memphis",
                source="Realtor",
            ),
        ]
    )

    result = BatchProcessor(
        FakeDecisionWorkflow(),
    ).process(request)

    assert result.total_reviews == 2
