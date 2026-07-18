"""
MF-206.0 scoring factors.

Defines the investment decision dimensions used by the scoring engine.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class ScoringFactors:
    cash_flow: float = 0.0
    appreciation: float = 0.0
    risk: float = 0.0
    tax_efficiency: float = 0.0
    liquidity: float = 0.0
