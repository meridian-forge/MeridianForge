"""
Investment thesis builder service.

Creates structured investment reasoning from investor packages.
"""

from meridianforge.intelligence.investment_thesis import (
    InvestmentThesis,
)
from meridianforge.product.investor_package import (
    InvestorPackage,
)


class InvestmentThesisBuilder:
    """
    Builds investment thesis objects.
    """

    def build(
        self,
        package: InvestorPackage,
    ) -> InvestmentThesis:
        """
        Create an investment thesis from an investor package.
        """

        thesis = InvestmentThesis(
            recommendation=package.recommendation,
            confidence=package.confidence,
            rationale=(
                f"{package.recommendation.upper()} recommendation "
                f"for {package.property_name}"
            ),
            investor_fit=self._determine_investor_fit(
                package.recommendation,
            ),
        )

        if package.confidence >= 0.80:
            thesis.add_strength(
                "High confidence investment recommendation",
            )
        else:
            thesis.add_risk(
                "Lower confidence recommendation requires review",
            )

        thesis.add_strength(
            "Structured investor decision package available",
        )

        return thesis

    def _determine_investor_fit(
        self,
        recommendation: str,
    ) -> str:
        """
        Determine basic investor fit.
        """

        if recommendation.upper() == "BUY":
            return "Suitable for active acquisition investors"

        if recommendation.upper() == "WATCH":
            return "Suitable for investors monitoring opportunities"

        return "Requires additional investor review"
