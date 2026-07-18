from .actions import recommended_action
from .confidence import confidence_from_score
from .models import DecisionType, InvestmentDecision, RiskLevel
from .rationale import build_rationale


class DecisionEngine:

    def evaluate(
        self,
        property_id: str,
        score: float,
        risk_level: RiskLevel,
    ) -> InvestmentDecision:

        if score >= 75:
            decision = DecisionType.BUY
        elif score >= 60:
            decision = DecisionType.WATCH
        else:
            decision = DecisionType.PASS

        return InvestmentDecision(
            property_id=property_id,
            decision=decision,
            score=score,
            confidence=confidence_from_score(score),
            risk_level=risk_level,
            rationale=build_rationale(
                score,
                risk_level.value,
            ),
            recommended_action=recommended_action(decision),
        )
