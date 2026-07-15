"""
Investment strategy definitions.
"""

from enum import StrEnum


class InvestmentStrategy(StrEnum):
    """
    Supported investor strategies.
    """

    CONSERVATIVE = "CONSERVATIVE"

    BALANCED = "BALANCED"

    GROWTH = "GROWTH"

    CASH_FLOW = "CASH_FLOW"

    VALUE_ADD = "VALUE_ADD"
