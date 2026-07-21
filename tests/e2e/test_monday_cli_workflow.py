"""
End-to-end validation of the Monday CLI workflow.

Goal:
User can execute a single CLI command against an example property
and receive an investor recommendation.
"""

from pathlib import Path

from openpyxl import Workbook

from meridianforge.models.domain.investment_strategy import (
    InvestmentStrategy,
)
from meridianforge.models.domain.investor_profile import (
    InvestorProfile,
)
from meridianforge.services.acquisition_execution_service import (
    AcquisitionExecutionService,
)
from meridianforge.services.acquisition_file_service import (
    AcquisitionFileService,
)


def test_monday_cli_workflow(tmp_path: Path):
    workbook = Workbook()
    sheet = workbook.active

    sheet["A1"] = "purchase_price"
    sheet["B1"] = "250000"

    sheet["A2"] = "rent"
    sheet["B2"] = "2500"

    sheet["A3"] = "market"
    sheet["B3"] = "Jacksonville"

    file_path = tmp_path / "property.xlsx"
    workbook.save(file_path)

    opportunity = AcquisitionFileService().load(str(file_path))

    investor = InvestorProfile(
        name="Monday Investor",
        strategy=InvestmentStrategy.CASH_FLOW,
    )

    result = AcquisitionExecutionService().execute(
        opportunity,
        investor,
    )

    assert len(result.review.cards) >= 1
    assert result.review.cards[0].recommendation in {
        "BUY",
        "WATCH",
    }
