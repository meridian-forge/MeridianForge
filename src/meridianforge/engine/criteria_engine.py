"""
Investor criteria evaluation engine.

Determines whether an analyzed property
matches an investor profile.
"""

from meridianforge.models.domain.investor_profile import (
    InvestorProfile,
)
from meridianforge.models.results.analysis_result import (
    AnalysisResult,
)
from meridianforge.models.results.deal_evaluation import (
    DealEvaluation,
)


class CriteriaEngine:
    """
    Evaluates investment opportunities
    against investor requirements.
    """

    @staticmethod
    def evaluate(
        profile: InvestorProfile,
        analysis: AnalysisResult,
    ) -> DealEvaluation:
        """
        Compare property analysis against
        investor criteria.
        """

        reasons: list[str] = []

        failed: list[str] = []

        passed_checks = 0

        total_checks = 4

        if analysis.dscr >= profile.minimum_dscr:
            reasons.append(
                "DSCR requirement met",
            )
            passed_checks += 1
        else:
            failed.append(
                "DSCR below minimum",
            )

        if analysis.cap_rate >= profile.minimum_cap_rate:
            reasons.append(
                "Cap rate requirement met",
            )
            passed_checks += 1
        else:
            failed.append(
                "Cap rate below minimum",
            )

        if analysis.cash_on_cash_return >= profile.minimum_cash_on_cash:
            reasons.append(
                "Cash-on-cash requirement met",
            )
            passed_checks += 1
        else:
            failed.append(
                "Cash-on-cash below minimum",
            )

        if analysis.purchase_price <= profile.maximum_purchase_price:
            reasons.append(
                "Purchase price within limit",
            )
            passed_checks += 1
        else:
            failed.append(
                "Purchase price exceeds maximum",
            )

        score = (passed_checks / total_checks) * 100

        return DealEvaluation(
            qualified=len(failed) == 0,
            score=score,
            reasons=reasons,
            failed_criteria=failed,
        )
