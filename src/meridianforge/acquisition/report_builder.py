"""
Acquisition report builder.

MF-336.3

Transforms acquisition intelligence
into an investor-facing report.
"""

from meridianforge.acquisition.report import (
    AcquisitionReport,
)

from meridianforge.acquisition.result import (
    AcquisitionResult,
)

from meridianforge.acquisition.snapshot import (
    UnderwritingSnapshot,
)


class AcquisitionReportBuilder:
    """
    Builds investor reports from acquisition results.
    """

    @staticmethod
    def build(
        result: AcquisitionResult,
    ) -> AcquisitionReport:
        """
        Convert acquisition result into report.
        """

        if result.thesis is None:
            raise ValueError(
                "Investment thesis required "
                "before report generation."
            )

        analysis = result.analysis

        opportunity = result.opportunity

        property_address = (
            f"{opportunity.address}, "
            f"{opportunity.city}, "
            f"{opportunity.state} "
            f"{opportunity.zip_code}"
        )

        snapshot = UnderwritingSnapshot(
            purchase_price=analysis.purchase_price,
            monthly_rent=analysis.monthly_rent,
            annual_cash_flow=(
                analysis.annual_cash_flow
            ),
            cap_rate=analysis.cap_rate,
            cash_on_cash_return=(
                analysis.cash_on_cash_return
            ),
            dscr=analysis.dscr,
            monthly_cash_flow=(
                analysis.monthly_cash_flow
            ),
        )

        return AcquisitionReport(
            property_address=property_address,
            recommendation=result.recommendation,
            score=result.score,
            confidence=result.confidence,
            purchase_price=analysis.purchase_price,
            monthly_rent=analysis.monthly_rent,
            annual_cash_flow=(
                analysis.annual_cash_flow
            ),
            cap_rate=analysis.cap_rate,
            cash_on_cash_return=(
                analysis.cash_on_cash_return
            ),
            dscr=analysis.dscr,
            thesis=result.thesis,
            snapshot=snapshot,
            risks=result.warnings.copy(),
        )
