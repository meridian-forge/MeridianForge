from datetime import date

from meridianforge.portfolio.operations.calendar import (
    PortfolioOperatingCalendar,
)


def test_monthly_portfolio_review_event():

    calendar = PortfolioOperatingCalendar()

    event = calendar.monthly_review(
        date(2026, 8, 1),
    )

    assert event.title == "Monthly Portfolio Review"

    assert event.category == "PERFORMANCE"

    assert event.priority == "MEDIUM"
