"""
Investor fit scoring engine.

Evaluates how well an investment opportunity aligns
with investor preferences.
"""

from dataclasses import dataclass

from meridianforge.intelligence.investor_profile import (
    InvestorProfile,
)


@dataclass(slots=True)
class InvestorFitScore:
    """
    Represents investor opportunity alignment.
    """

    cash_flow_fit: float
    appreciation_fit: float
    tax_fit: float
    risk_fit: float
    overall_score: float


class InvestorFitEngine:
    """
    Calculates investor opportunity fit.
    """

    def evaluate(
        self,
        profile: InvestorProfile,
        cash_flow_score: float,
        appreciation_score: float,
        tax_score: float,
        risk_score: float,
    ) -> InvestorFitScore:
        """
        Calculate weighted investor fit.
        """

        cash_flow_weight = profile.target_cash_flow
        appreciation_weight = profile.appreciation_priority
        tax_weight = profile.tax_focus

        remaining_weight = (
            1.0
            - cash_flow_weight
            - appreciation_weight
            - tax_weight
        )

        risk_weight = max(
            remaining_weight,
            0.0,
        )

        overall_score = (
            cash_flow_score * cash_flow_weight
            + appreciation_score * appreciation_weight
            + tax_score * tax_weight
            + risk_score * risk_weight
        )

        return InvestorFitScore(
            cash_flow_fit=cash_flow_score,
            appreciation_fit=appreciation_score,
            tax_fit=tax_score,
            risk_fit=risk_score,
            overall_score=overall_score,
        )
