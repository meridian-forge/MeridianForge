from meridianforge.models.domain.acquisition import Acquisition
from meridianforge.models.domain.address import Address
from meridianforge.models.domain.assumptions import Assumptions
from meridianforge.models.domain.expenses import Expenses
from meridianforge.models.domain.financing import Financing
from meridianforge.models.domain.income import Income
from meridianforge.models.domain.metadata import Metadata
from meridianforge.models.domain.property import Property
from meridianforge.models.results.deal_evaluation import DealEvaluation
from meridianforge.models.results.ranked_deal import RankedDeal
from meridianforge.product.workflow import (
    InvestorWorkflowService,
)


def test_workflow_creates_investor_review():

    property = Property(
        address=Address(
            street="123 Main St",
            city="Jacksonville",
            state="FL",
            zip_code="32210",
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
            insurance=1500,
        ),
        assumptions=Assumptions(),
        metadata=Metadata(
            provider="Test Provider",
            imported_at="2026-07-19",
        ),
    )

    deal = RankedDeal(
        rank=1,
        property=property,
        evaluation=DealEvaluation(
            qualified=True,
            score=90,
            reasons=[
                "Strong cash flow",
            ],
            failed_criteria=[],
        ),
    )

    review = InvestorWorkflowService().create_review(deal)

    assert review.rank == 1
    assert review.property_address == "123 Main St, Jacksonville, FL 32210"
    assert review.recommendation == "BUY"
    assert review.confidence == 0.90
    assert review.is_actionable()
    card = InvestorWorkflowService().create_decision_card(review)

    assert card.rank == 1
    assert card.property_address == review.property_address
    assert card.recommendation == "BUY"
    assert card.confidence == 0.90
    assert card.strengths == ["Strong cash flow"]
    assert card.risks == []
    assert card.is_buy_candidate()
