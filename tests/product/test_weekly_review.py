from meridianforge.product.decision_card import InvestorDecisionCard
from meridianforge.product.weekly_review import WeeklyInvestorReview


def test_buy_candidates():

    buy = InvestorDecisionCard(
        rank=1,
        property_address="123 Main St",
        recommendation="BUY",
        confidence=0.90,
    )

    watch = InvestorDecisionCard(
        rank=2,
        property_address="456 Oak Ave",
        recommendation="WATCH",
        confidence=0.60,
    )

    report = WeeklyInvestorReview(
        cards=[
            buy,
            watch,
        ]
    )

    assert len(report.buy_candidates()) == 1
    assert len(report.watch_candidates()) == 1
