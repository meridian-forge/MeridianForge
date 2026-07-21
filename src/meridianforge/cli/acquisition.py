import argparse

from meridianforge.models.domain.investment_strategy import (
    InvestmentStrategy,
)
from meridianforge.models.domain.investor_profile import (
    InvestorProfile,
)
from meridianforge.reporting.acquisition_report import (
    AcquisitionReportFormatter,
)
from meridianforge.services.acquisition_execution_service import (
    AcquisitionExecutionService,
)
from meridianforge.services.acquisition_file_service import (
    AcquisitionFileService,
)


def run_acquisition(
    args: argparse.Namespace,
) -> None:
    """
    Execute acquisition analysis from CLI.
    """

    opportunity = AcquisitionFileService().load(
        args.file,
    )

    investor = InvestorProfile(
        name="Default Investor",
        strategy=InvestmentStrategy.CASH_FLOW,
    )

    result = AcquisitionExecutionService().execute(
        opportunity,
        investor,
    )

    report = AcquisitionReportFormatter.format(
        result.review,
    )

    print(report)
