"""
MF-206.0 scoring weights.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class ScoringWeights:
    cash_flow: float = 0.30
    appreciation: float = 0.25
    risk: float = 0.20
    tax_efficiency: float = 0.15
    liquidity: float = 0.10
