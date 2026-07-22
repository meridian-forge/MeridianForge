"""
Investor match engine.

Connects acquisition opportunities with investor profiles.
"""

from dataclasses import dataclass

from meridianforge.acquisition.opportunity import (
    Opportunity,
)
from meridianforge.intelligence.investor_fit_engine import (
    InvestorFitEngine,
    InvestorFitScore,
)
from meridianforge.intelligence.investor_profile import (
    InvestorProfile,
)


@dataclass(slots=True)
class InvestorMatch:
    """
    Represents investor opportunity alignment.
    """

    investor_name: str
    property_address: str
    fit_score: InvestorFitScore


class InvestorMatchEngine:
    """
    Matches opportunities to investors.
    """

    def match(
        self,
        opportunity: Opportunity,
        investor: InvestorProfile,
    ) -> InvestorMatch:
        """
        Calculate investor opportunity alignment.
        """

        score = InvestorFitEngine().evaluate(
            profile=investor,
            cash_flow_score=min(
                opportunity.cap_rate / 0.08,
                1.0,
            ),
            appreciation_score=0.70,
            tax_score=0.75,
            risk_score=0.80,
        )

        return InvestorMatch(
            investor_name=investor.name,
            property_address=opportunity.address,
            fit_score=score,
        )
