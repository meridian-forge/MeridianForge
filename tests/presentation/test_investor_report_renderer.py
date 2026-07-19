from meridianforge.presentation.investor_report_renderer import (
    InvestorReportRenderer,
)
from meridianforge.product.decision_card import InvestorDecisionCard
from meridianforge.product.weekly_review import WeeklyInvestorReview


def test_renderer_generates_report():

    review = WeeklyInvestorReview(
        cards=[
            InvestorDecisionCard(
                rank=1,
                property_address="123 Main St",
                recommendation="BUY",
                confidence=0.91,
                strengths=[
                    "Strong cash flow",
                ],
                risks=[
                    "Older roof",
                ],
            ),
        ]
    )

    output = InvestorReportRenderer().render(review)

    assert "MERIDIAN FORGE" in output

    assert "123 Main St" in output

    assert "BUY" in output

    assert "Older roof" in output
