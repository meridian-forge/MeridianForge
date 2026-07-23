from meridianforge.acquisition.dashboard import (
    AcquisitionDashboard,
)


def test_dashboard_creation():

    dashboard = AcquisitionDashboard(
        total_deals=10,
        buy_candidates=4,
        review_candidates=6,
        average_score=72,
        average_confidence=0.82,
        high_risk_count=1,
    )

    assert dashboard.total_deals == 10

    assert dashboard.buy_candidates == 4

    assert dashboard.high_risk_count == 1
