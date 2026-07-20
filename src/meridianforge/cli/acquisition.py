from pathlib import Path

from meridianforge.opportunity.models import Opportunity
from meridianforge.services.acquisition_execution_service import (
    AcquisitionExecutionService,
)
from meridianforge.models.domain.investor_profile import (
    InvestorProfile,
)
from meridianforge.models.domain.investment_strategy import (
    InvestmentStrategy,
)


def run_acquisition(args) -> None:
    """
    Execute acquisition analysis from CLI.
    """

    opportunity = Opportunity(
        source_file=str(Path(args.file)),
        fields={},
        confidence=0.0,
    )

    investor = InvestorProfile(
        name="Default Investor",
        strategy=InvestmentStrategy.CASH_FLOW,
    )

    result = AcquisitionExecutionService().execute(
        opportunity,
        investor,
    )

    print(
        result.review.cards[0]
    )
