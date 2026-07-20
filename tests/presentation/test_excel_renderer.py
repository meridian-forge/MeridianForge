from pathlib import Path

from openpyxl import load_workbook

from meridianforge.presentation.excel_renderer import (
    ExcelInvestorReportRenderer,
)
from meridianforge.product.decision_card import InvestorDecisionCard
from meridianforge.product.weekly_review import WeeklyInvestorReview


def test_excel_renderer_generates_workbook(tmp_path: Path):

    review = WeeklyInvestorReview(
        cards=[
            InvestorDecisionCard(
                rank=1,
                property_address="123 Main St",
                recommendation="BUY",
                confidence=0.91,
                strengths=[
                    "Strong cash flow",
                ],
                risks=[
                    "Older roof",
                ],
            ),
        ]
    )

    output_file = tmp_path / "investor_summary.xlsx"

    result = ExcelInvestorReportRenderer().render(
        review,
        output_file,
    )

    assert result.exists()

    workbook = load_workbook(result)

    worksheet = workbook["Investor Review"]

    assert worksheet["A2"].value == 1
    assert worksheet["B2"].value == "123 Main St"
    assert worksheet["C2"].value == "BUY"
    assert worksheet["D2"].value == "91%"
