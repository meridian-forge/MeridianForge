"""
Acquisition decision engine.

MF-334.2

Converts underwriting results and scores
into actionable acquisition decisions.
"""

from meridianforge.acquisition.criteria import (
    AcquisitionCriteria,
)
from meridianforge.acquisition.decision import (
    AcquisitionDecision,
)
from meridianforge.acquisition.risk import (
    RiskFlag,
    RiskSeverity,
)
from meridianforge.models.results.analysis_result import (
    AnalysisResult,
)


class AcquisitionDecisionEngine:
    """
    Generates acquisition recommendations.
    """

    def evaluate(
        self,
        analysis: AnalysisResult,
        score: float,
        criteria: AcquisitionCriteria,
    ) -> AcquisitionDecision:
        """
        Evaluate underwriting outcome.
        """

        reasons: list[str] = []
        risks: list[RiskFlag] = []

        if analysis.dscr >= criteria.minimum_dscr:
            reasons.append("DSCR meets target")
        else:
            risks.append(
                RiskFlag(
                    code="LOW_DSCR",
                    message=("Debt service coverage " "below target"),
                    severity=RiskSeverity.HIGH,
                )
            )

        if analysis.cap_rate >= criteria.minimum_cap_rate:
            reasons.append("Cap rate meets target")
        else:
            risks.append(
                RiskFlag(
                    code="LOW_CAP_RATE",
                    message=("Cap rate below minimum"),
                    severity=RiskSeverity.MEDIUM,
                )
            )

        if analysis.cash_on_cash_return >= criteria.minimum_cash_return:
            reasons.append("Cash return meets target")
        else:
            risks.append(
                RiskFlag(
                    code="LOW_CASH_RETURN",
                    message=("Cash-on-cash return " "below target"),
                    severity=RiskSeverity.MEDIUM,
                )
            )

        status = (
            "BUY"
            if score >= 70
            and not any(risk.severity == RiskSeverity.HIGH for risk in risks)
            else "REVIEW"
        )

        return AcquisitionDecision(
            status=status,
            score=score,
            reasons=reasons,
            risks=risks,
        )
