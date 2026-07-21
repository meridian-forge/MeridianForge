"""
Investment decision one-page brief.

Creates investor-facing justification
for BUY / WATCH / PASS decisions.
"""

from dataclasses import dataclass, field

from meridianforge.product.decision_card import (
    InvestorDecisionCard,
)


@dataclass(slots=True)
class DecisionBrief:
    """
    Investor decision document.
    """

    recommendation: str

    property_address: str

    confidence: float

    strengths: list[str] = field(
        default_factory=list,
    )

    risks: list[str] = field(
        default_factory=list,
    )

    investor_notes: list[str] = field(
        default_factory=list,
    )


class DecisionBriefBuilder:
    """
    Builds investment decision briefs.
    """

    @staticmethod
    def build(
        card: InvestorDecisionCard,
    ) -> DecisionBrief:

        investor_notes = [
            "Decision based on available opportunity data.",
            "Validate assumptions before execution.",
            "Review financing and liquidity impact.",
        ]

        return DecisionBrief(
            recommendation=card.recommendation,
            property_address=card.property_address,
            confidence=card.confidence,
            strengths=list(card.strengths),
            risks=list(card.risks),
            investor_notes=investor_notes,
        )
