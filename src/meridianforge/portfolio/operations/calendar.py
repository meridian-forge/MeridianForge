"""
Portfolio operating calendar engine.

MF-348.1

Generates scheduled operating events
for investor portfolio management.
"""

from dataclasses import dataclass
from datetime import date


@dataclass(slots=True)
class PortfolioCalendarEvent:
    """
    Scheduled portfolio operating event.
    """

    title: str

    category: str

    due_date: date

    priority: str

    description: str


class PortfolioOperatingCalendar:
    """
    Builds portfolio operating calendar events.
    """

    def create_event(
        self,
        title: str,
        category: str,
        due_date: date,
        priority: str,
        description: str,
    ) -> PortfolioCalendarEvent:
        """
        Create calendar event.
        """

        return PortfolioCalendarEvent(
            title=title,
            category=category,
            due_date=due_date,
            priority=priority,
            description=description,
        )

    def monthly_review(
        self,
        due_date: date,
    ) -> PortfolioCalendarEvent:
        """
        Generate monthly portfolio review.
        """

        return self.create_event(
            title="Monthly Portfolio Review",
            category="PERFORMANCE",
            due_date=due_date,
            priority="MEDIUM",
            description="Review rental performance, cash flow, and portfolio health.",
        )

    def acquisition_review(
        self,
        due_date: date,
    ) -> PortfolioCalendarEvent:
        """
        Generate acquisition pipeline review.
        """

        return self.create_event(
            title="Acquisition Pipeline Review",
            category="ACQUISITION",
            due_date=due_date,
            priority="HIGH",
            description="Evaluate new investment opportunities.",
        )
