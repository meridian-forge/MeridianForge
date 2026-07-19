from meridianforge.reporting.monday_dashboard import (
    MondayDashboardGenerator,
)


def test_dashboard_generation() -> None:

    dashboard = MondayDashboardGenerator().generate(
        {
            "total_opportunities": 5,
            "buy_count": 2,
            "watch_count": 3,
            "average_score": 82,
            "top_opportunity": {
                "name": "Property A",
                "score": 95,
            },
        }
    )

    assert "Property A" in dashboard
    assert "BUY Candidates: 2" in dashboard
