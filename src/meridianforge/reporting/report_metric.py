"""
Report metric domain model.

MF-343.1

Represents a single investor-facing metric
inside a portfolio report.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class ReportMetric:
    """
    Individual report metric.

    Example:
        Annual Cash Flow: $42,000
    """

    name: str

    value: str

    description: str = ""
