"""
Investment report builder.

Creates investor-facing reports
from underwriting outputs.
"""

from meridianforge.engine.risk import RiskEngine
from meridianforge.engine.stress_test import StressTestEngine
from meridianforge.engine.underwriting_engine import UnderwritingEngine
from meridianforge.models.domain.property import Property
from meridianforge.models.domain.scenario import Scenario
from meridianforge.models.results.report import InvestmentReport
from meridianforge.models.results.risk_rating import RiskRating


class ReportBuilder:
    """
    Builds complete investment reports.
    """

    @staticmethod
    def build(
        property_data: Property,
    ) -> InvestmentReport:
        """
        Generate investor report.
        """

        analysis = UnderwritingEngine.analyze(
            property_data,
        )

        stress_result = StressTestEngine.analyze(
            property_data,
            Scenario(
                name="Default Stress Test",
                expense_change_percent=0.25,
                vacancy_change_percent=0.10,
                interest_rate_change_percent=0.01,
            ),
        )

        risk_rating = RiskEngine.evaluate(
            stress_result,
        )

        recommendation = "PASS" if risk_rating == RiskRating.SAFE else "REVIEW"

        summary = (
            "Property meets investment criteria."
            if recommendation == "PASS"
            else "Property requires further review " "due to downside risk."
        )

        return InvestmentReport(
            property=property_data,
            analysis=analysis,
            stress_result=stress_result,
            risk_rating=risk_rating,
            recommendation=recommendation,
            summary=summary,
        )
