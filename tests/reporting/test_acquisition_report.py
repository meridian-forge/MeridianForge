from meridianforge.product.decision_card import (
    InvestorDecisionCard,
)
from meridianforge.product.weekly_review import (
    WeeklyInvestorReview,
)
from meridianforge.reporting.acquisition_report import (
    AcquisitionReportFormatter,
)


def test_acquisition_report_formatter():

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
            )
        ]
    )

    report = AcquisitionReportFormatter.format(
        review,
    )

    assert "123 Main St" in report
    assert "BUY" in report
    assert "91%" in report
    assert "Strong cash flow" in report
    assert "Older roof" in report
