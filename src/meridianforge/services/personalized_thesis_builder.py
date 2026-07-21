"""
Personalized investment thesis builder.

Creates investor-specific thesis narratives using
investor profile and fit scoring.
"""

from meridianforge.intelligence.investment_thesis import (
    InvestmentThesis,
)
from meridianforge.intelligence.investor_fit_engine import (
    InvestorFitScore,
)
from meridianforge.intelligence.investor_profile import (
    InvestorProfile,
)


class PersonalizedThesisBuilder:
    """
    Builds investment theses personalized to investors.
    """

    def build(
        self,
        profile: InvestorProfile,
        fit_score: InvestorFitScore,
        property_name: str,
        recommendation: str,
    ) -> InvestmentThesis:
        """
        Generate a personalized investment thesis.
        """

        rationale = (
            f"{property_name} aligns with "
            f"{profile.strategy} strategy with "
            f"{fit_score.overall_score:.0%} investor fit."
        )

        strengths = [
            (f"Investor alignment score: " f"{fit_score.overall_score:.0%}"),
            (f"Cash flow fit: " f"{fit_score.cash_flow_fit:.0%}"),
            (f"Tax fit: " f"{fit_score.tax_fit:.0%}"),
        ]

        risks = [
            (
                f"Risk profile requires monitoring "
                f"for {profile.risk_tolerance} investors."
            ),
        ]

        return InvestmentThesis(
            recommendation=recommendation,
            confidence=fit_score.overall_score,
            rationale=rationale,
            strengths=strengths,
            risks=risks,
            investor_fit=(f"{profile.name}: " f"{fit_score.overall_score:.0%}"),
        )
