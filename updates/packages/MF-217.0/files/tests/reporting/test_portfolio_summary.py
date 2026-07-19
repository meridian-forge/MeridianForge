from meridianforge.reporting.portfolio_summary import (
    PortfolioSummary,
)


def test_portfolio_summary() -> None:

    summary = PortfolioSummary().summarize(
        [
            {
                "name": "A",
                "status": "BUY",
                "score": 90,
            },
            {
                "name": "B",
                "status": "WATCH",
                "score": 70,
            },
        ]
    )

    assert summary["total_opportunities"] == 2
    assert summary["buy_count"] == 1
    assert summary["watch_count"] == 1
    assert summary["average_score"] == 80
