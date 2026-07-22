"""
Acquisition package workflow.

Coordinates the complete acquisition intelligence pipeline.
"""

from pathlib import Path

from meridianforge.acquisition.opportunity import Opportunity
from meridianforge.intelligence.investor_profile import InvestorProfile
from meridianforge.matching.investor_match_engine import (
    InvestorMatchEngine,
)
from meridianforge.product.investor_package import InvestorPackage
from meridianforge.scoring.deal_score_engine import (
    DealScoreEngine,
)
from meridianforge.workflows.investor_package_workflow import (
    InvestorPackageWorkflow,
)


class AcquisitionPackageWorkflow:
    """
    End-to-end acquisition workflow.
    """

    def __init__(self) -> None:
        self.deal_score_engine = DealScoreEngine()
        self.match_engine = InvestorMatchEngine()
        self.package_workflow = InvestorPackageWorkflow()

    def generate(
        self,
        opportunity: Opportunity,
        investor: InvestorProfile,
        output_directory: Path,
    ) -> InvestorPackage:
        """
        Generate a complete investor package from an opportunity.
        """

        deal_score = self.deal_score_engine.evaluate(
            cash_flow_score=min(
                opportunity.monthly_cash_flow / 1500.0,
                1.0,
            ),
            cap_rate_score=min(
                opportunity.cap_rate / 0.08,
                1.0,
            ),
            risk_score=0.80,
            market_score=0.75,
        )

        match = self.match_engine.match(
            opportunity=opportunity,
            investor=investor,
        )

        recommendation = "BUY" if deal_score.overall_score >= 0.75 else "WATCH"

        return self.package_workflow.generate(
            package_id="AUTO-001",
            property_name=opportunity.address,
            recommendation=recommendation,
            confidence=match.fit_score.overall_score,
            output_directory=output_directory,
        )
