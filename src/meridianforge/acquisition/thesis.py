"""
Investment thesis model.

MF-335.1

Represents investor-facing reasoning
generated from acquisition intelligence.
"""

from dataclasses import dataclass, field


@dataclass(slots=True)
class InvestmentThesis:
    """
    Human-readable investment conclusion.
    """

    property_address: str

    recommendation: str

    score: float

    confidence: float

    summary: str

    highlights: list[str] = field(
        default_factory=list,
    )

    risks: list[str] = field(
        default_factory=list,
    )
