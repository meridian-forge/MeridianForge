from meridianforge.acquisition.dashboard_builder import (
    AcquisitionDashboardBuilder,
)

from meridianforge.acquisition.result import (
    AcquisitionResult,
)


def test_dashboard_builder():

    results = [
        AcquisitionResult(
            opportunity="A",
            analysis="analysis",
            score=100,
            ranking=1,
            recommendation="BUY",
            confidence=1.0,
            warnings=[],
        ),
        AcquisitionResult(
            opportunity="B",
            analysis="analysis",
            score=60,
            ranking=2,
            recommendation="REVIEW",
            confidence=0.7,
            warnings=[
                "Risk detected",
            ],
        ),
    ]

    dashboard = AcquisitionDashboardBuilder.build(
        results
    )

    assert dashboard.total_deals == 2
    assert dashboard.buy_candidates == 1
    assert dashboard.review_candidates == 1
    assert dashboard.average_score == 80
    assert dashboard.high_risk_count == 1
