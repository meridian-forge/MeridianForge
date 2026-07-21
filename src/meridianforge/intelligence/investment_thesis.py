"""
Investment thesis model.

Defines structured reasoning behind an investment recommendation.
"""

from dataclasses import dataclass, field


@dataclass(slots=True)
class InvestmentThesis:
    """
    Structured investment rationale for a property decision.
    """

    recommendation: str
    confidence: float
    rationale: str
    strengths: list[str] = field(
        default_factory=list,
    )
    risks: list[str] = field(
        default_factory=list,
    )
    investor_fit: str = ""

    def add_strength(
        self,
        strength: str,
    ) -> None:
        """
        Add an investment strength.
        """

        self.strengths.append(
            strength,
        )

    def add_risk(
        self,
        risk: str,
    ) -> None:
        """
        Add an investment risk.
        """

        self.risks.append(
            risk,
        )
