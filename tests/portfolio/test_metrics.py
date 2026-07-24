from meridianforge.portfolio.metrics import (
    PortfolioMetrics,
)


def test_portfolio_metrics_creation() -> None:

    metrics = PortfolioMetrics(
        total_properties=5,
        total_monthly_cash_flow=2500.0,
        total_annual_cash_flow=30000.0,
        average_cap_rate=8.4,
        average_cash_on_cash=12.5,
        average_dscr=1.42,
        average_score=91.3,
        average_confidence=0.94,
        buy_count=4,
        review_count=1,
        reject_count=0,
    )

    assert metrics.total_properties == 5
    assert metrics.total_monthly_cash_flow == 2500.0
    assert metrics.total_annual_cash_flow == 30000.0
    assert metrics.average_cap_rate == 8.4
    assert metrics.average_cash_on_cash == 12.5
    assert metrics.average_dscr == 1.42
    assert metrics.average_score == 91.3
    assert metrics.average_confidence == 0.94
    assert metrics.buy_count == 4
    assert metrics.review_count == 1
    assert metrics.reject_count == 0
