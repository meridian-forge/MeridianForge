from meridianforge.portfolio.intelligence.action_generator import (
    PortfolioActionGenerator,
)
from meridianforge.portfolio.intelligence.alerts import (
    PortfolioAlert,
)


def test_alert_generates_high_priority_action():

    generator = PortfolioActionGenerator()

    alert = PortfolioAlert(
        category="DEBT",
        severity="HIGH",
        message="DSCR requires attention",
        recommendation="Review financing",
    )

    action = generator.generate(
        alert,
    )

    assert action.action_type == "FINANCING_REVIEW"

    assert action.priority == "HIGH"

    assert action.description == "DSCR requires attention"


def test_quality_alert_generates_portfolio_review():

    generator = PortfolioActionGenerator()

    alert = PortfolioAlert(
        category="QUALITY",
        severity="MEDIUM",
        message="Portfolio quality requires review",
        recommendation="Review assets",
    )

    action = generator.generate(
        alert,
    )

    assert action.action_type == "PORTFOLIO_REVIEW"

    assert action.priority == "MEDIUM"
