from dataclasses import dataclass

from meridianforge.intelligence.recommendation.explanations import (
    generate_explanation,
)
from meridianforge.intelligence.recommendation.rules import (
    evaluate_rules,
)


@dataclass
class Recommendation:
    action: str
    reasons: list[str]


def recommend(
    cash_flow: float,
    dscr: float,
    appreciation_score: float,
) -> Recommendation:
    """
    Generate investment recommendation.
    """

    action = evaluate_rules(
        cash_flow,
        dscr,
        appreciation_score,
    )

    return Recommendation(
        action=action,
        reasons=generate_explanation(action),
    )
