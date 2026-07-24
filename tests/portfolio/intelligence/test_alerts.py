from meridianforge.portfolio.intelligence.alerts import (
    PortfolioAlertFactory,
)


def test_alert_factory_creates_alert():

    alert = PortfolioAlertFactory.create(
        category="RISK",
        severity="HIGH",
        message="Test alert",
        recommendation="Review portfolio",
    )

    assert alert.category == "RISK"

    assert alert.severity == "HIGH"
