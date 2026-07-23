"""
Investment thesis generator.

MF-335.2

Transforms acquisition intelligence
into investor-facing reasoning.
"""

from meridianforge.acquisition.result import (
    AcquisitionResult,
)

from meridianforge.acquisition.thesis import (
    InvestmentThesis,
)


class InvestmentThesisGenerator:
    """
    Generates investor explanations.
    """

    @staticmethod
    def generate(
        result: AcquisitionResult,
    ) -> InvestmentThesis:
        """
        Create investment thesis from
        acquisition result.
        """

        opportunity = result.opportunity

        property_address = (
            f"{opportunity.address}, "
            f"{opportunity.city}, "
            f"{opportunity.state} "
            f"{opportunity.zip_code}"
        )

        highlights: list[str] = []

        analysis = result.analysis

        if analysis.dscr >= 1.20:
            highlights.append("DSCR exceeds acquisition target")

        if analysis.cap_rate >= 0.05:
            highlights.append("Cap rate meets minimum threshold")

        if analysis.cash_on_cash_return >= 0.08:
            highlights.append("Cash return meets target")

        risks = result.warnings.copy()

        if result.recommendation == "BUY":
            summary = "Strong acquisition candidate " "based on underwriting metrics."
        else:
            summary = "Property requires additional " "review before acquisition."

        return InvestmentThesis(
            property_address=property_address,
            recommendation=result.recommendation,
            score=result.score,
            confidence=result.confidence,
            summary=summary,
            highlights=highlights,
            risks=risks,
        )
