from pathlib import Path

from openpyxl import Workbook

from meridianforge.services.acquisition_file_service import (
    AcquisitionFileService,
)
from meridianforge.services.acquisition_execution_service import (
    AcquisitionExecutionService,
)
from meridianforge.models.domain.investor_profile import (
    InvestorProfile,
)
from meridianforge.models.domain.investment_strategy import (
    InvestmentStrategy,
)
from meridianforge.reporting.acquisition_report import (
    AcquisitionReportFormatter,
)


def test_end_to_end_acquisition_excel_workflow(
    tmp_path: Path,
):

    file_path = tmp_path / "investment_property.xlsx"

    workbook = Workbook()

    sheet = workbook.active

    sheet["A1"] = "property_address"
    sheet["B1"] = "123 Main St"

    sheet["A2"] = "purchase_price"
    sheet["B2"] = "250000"

    sheet["A3"] = "market"
    sheet["B3"] = "Jacksonville"

    sheet["A4"] = "rent"
    sheet["B4"] = "2500"

    sheet["A5"] = "noi"
    sheet["B5"] = "18000"

    workbook.save(file_path)


    opportunity = AcquisitionFileService().load(
        str(file_path),
    )


    investor = InvestorProfile(
        name="Mahi",
        strategy=InvestmentStrategy.CASH_FLOW,
    )


    result = AcquisitionExecutionService().execute(
        opportunity,
        investor,
    )


    report = AcquisitionReportFormatter.format(
        result.review,
    )


    assert "MERIDIAN FORGE" in report
    assert len(result.review.cards) > 0
