from pathlib import Path

from meridianforge.presentation.export_service import (
    InvestorReportExportService,
)
from meridianforge.product.decision_card import InvestorDecisionCard
from meridianforge.product.weekly_review import WeeklyInvestorReview


def test_export_service_generates_reports(tmp_path: Path):

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

    files = InvestorReportExportService().export(
        review,
        tmp_path,
    )

    assert len(files) == 4

    assert any(file.name == "investor_review.pdf" for file in files)

    assert (tmp_path / "investor_review.txt").exists()
    assert (tmp_path / "investor_review.md").exists()
    assert (tmp_path / "investor_review.xlsx").exists()
