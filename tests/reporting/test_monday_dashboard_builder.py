from meridianforge.product.decision_card import (
    InvestorDecisionCard,
)
from meridianforge.product.weekly_review import (
    WeeklyInvestorReview,
)
from meridianforge.reporting.monday_dashboard_builder import (
    MondayDashboardBuilder,
)


def test_dashboard_builder():

    review = WeeklyInvestorReview(
        cards=[
            InvestorDecisionCard(
                rank=1,
                property_address="A",
                recommendation="BUY",
                confidence=0.93,
            ),
            InvestorDecisionCard(
                rank=2,
                property_address="B",
                recommendation="WATCH",
                confidence=0.71,
            ),
            InvestorDecisionCard(
                rank=3,
                property_address="C",
                recommendation="PASS",
                confidence=0.20,
            ),
        ]
    )

    dashboard = MondayDashboardBuilder.build(
        review,
    )

    assert dashboard.total_reviewed == 3
    assert dashboard.buy_count == 1
    assert dashboard.watch_count == 1
    assert dashboard.pass_count == 1
    assert dashboard.top_opportunity.property_address == "A"
