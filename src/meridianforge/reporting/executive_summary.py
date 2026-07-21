"""
Executive summary generation for investor packages.
"""

from meridianforge.product.investor_package import InvestorPackage


class ExecutiveSummaryBuilder:
    """
    Builds a concise executive summary for an investor package.
    """

    def build(
        self,
        package: InvestorPackage,
    ) -> str:
        """
        Generate an executive summary.
        """

        return (
            f"Property: {package.property_name}\n"
            f"Recommendation: {package.recommendation.upper()}\n"
            f"Confidence: {package.confidence:.1%}\n"
            f"Artifacts Included: {len(package.artifacts)}"
        )
