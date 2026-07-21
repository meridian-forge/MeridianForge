from meridianforge.models.domain.acquisition import Acquisition
from meridianforge.models.domain.address import Address
from meridianforge.models.domain.assumptions import Assumptions
from meridianforge.models.domain.expenses import Expenses
from meridianforge.models.domain.financing import Financing
from meridianforge.models.domain.income import Income
from meridianforge.models.domain.metadata import Metadata
from meridianforge.models.domain.property import Property
from meridianforge.models.results.deal_evaluation import DealEvaluation
from meridianforge.models.results.investment_pipeline_result import (
    InvestmentPipelineResult,
)
from meridianforge.models.results.ranked_deal import RankedDeal
from meridianforge.services.acquisition_intelligence import (
    AcquisitionIntelligenceService,
)


def test_acquisition_intelligence_creates_buy_review_card():

    property_data = Property(
        address=Address(
            street="123 Main St",
            city="Jacksonville",
            state="FL",
            zip_code="32201",
        ),
        acquisition=Acquisition(
            purchase_price=250000,
            closing_costs=5000,
        ),
        financing=Financing(
            down_payment=50000,
            interest_rate=6.5,
            loan_term_years=30,
        ),
        income=Income(
            monthly_rent=2200,
        ),
        expenses=Expenses(
            taxes=3000,
            insurance=1200,
        ),
        assumptions=Assumptions(),
        metadata=Metadata(
            provider="Zillow",
            imported_at="2026-07-19",
        ),
    )

    result = InvestmentPipelineResult(
        ranked_deals=[
            RankedDeal(
                rank=1,
                property=property_data,
                evaluation=DealEvaluation(
                    qualified=True,
                    score=90,
                    reasons=[
                        "Strong DSCR",
                    ],
                ),
            )
        ]
    )

    review = AcquisitionIntelligenceService().create_review(
        result,
    )

    assert len(review.cards) == 1

    card = review.cards[0]

    assert card.recommendation == "BUY"
    assert card.confidence == 0.90
    assert card.property_address.startswith("123 Main St")
