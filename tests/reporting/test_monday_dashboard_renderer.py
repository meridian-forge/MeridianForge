from meridianforge.product.decision_card import (
    InvestorDecisionCard,
)
from meridianforge.product.weekly_review import (
    WeeklyInvestorReview,
)
from meridianforge.reporting.monday_dashboard_builder import (
    MondayDashboardBuilder,
)
from meridianforge.reporting.monday_dashboard_renderer import (
    MondayDashboardRenderer,
)


def test_dashboard_renderer():

    review = WeeklyInvestorReview(
        cards=[
            InvestorDecisionCard(
                rank=1,
                property_address="123 Main St",
                recommendation="BUY",
                confidence=0.90,
            ),
            InvestorDecisionCard(
                rank=2,
                property_address="456 Oak Ave",
                recommendation="WATCH",
                confidence=0.70,
            ),
        ]
    )

    dashboard = MondayDashboardBuilder.build(review)

    output = MondayDashboardRenderer.render(dashboard)

    assert "MERIDIAN FORGE" in output
    assert "BUY: 1" in output
    assert "123 Main St" in output
    assert "WATCH LIST" in output
