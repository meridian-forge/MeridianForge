from meridianforge.product.investor_review import (
    InvestorReview,
)


def test_investor_review_is_actionable():

    review = InvestorReview(
        rank=1,
        property_address="123 Main St Jacksonville FL",
        recommendation="BUY",
        confidence=0.90,
    )

    assert review.is_actionable()
