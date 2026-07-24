from meridianforge.portfolio.analytics import (
    PortfolioAnalytics,
)
from meridianforge.portfolio.intelligence.monitoring import (
    PortfolioMonitoringEngine,
)


def test_monitoring_detects_risk():

    analytics = PortfolioAnalytics(
        asset_count=2,
        total_purchase_price=500000,
        total_monthly_rent=4000,
        total_monthly_cash_flow=500,
        annual_cash_flow=6000,
        average_cap_rate=0.04,
        average_dscr=1.10,
        portfolio_score=70,
    )

    engine = PortfolioMonitoringEngine()

    alerts = engine.analyze(
        analytics,
    )

    assert len(alerts) >= 2

    assert alerts[0].severity == "HIGH"
