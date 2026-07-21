from meridianforge.product.decision_card import (
    InvestorDecisionCard,
)
from meridianforge.reporting.decision_brief import (
    DecisionBriefBuilder,
)


def test_decision_brief_builder():

    card = InvestorDecisionCard(
        rank=1,
        property_address="123 Main St",
        recommendation="BUY",
        confidence=0.91,
        strengths=[
            "Strong cash flow",
        ],
        risks=[
            "Roof replacement risk",
        ],
    )

    brief = DecisionBriefBuilder.build(
        card,
    )

    assert brief.recommendation == "BUY"

    assert brief.property_address == ("123 Main St")

    assert brief.confidence == 0.91

    assert "Strong cash flow" in brief.strengths
