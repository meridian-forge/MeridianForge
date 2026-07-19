from meridianforge.product.decision_card import (
    InvestorDecisionCard,
)


def test_buy_candidate():

    card = InvestorDecisionCard(
        rank=1,
        property_address="123 Main St, Jacksonville, FL 32210",
        recommendation="BUY",
        confidence=0.90,
        reasons=[
            "Strong cash flow",
        ],
        risks=[],
    )

    assert card.is_buy_candidate()
