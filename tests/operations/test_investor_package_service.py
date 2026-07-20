from pathlib import Path

from meridianforge.operations.investor_package_service import (
    InvestorPackageService,
)
from meridianforge.product.decision_card import InvestorDecisionCard
from meridianforge.product.weekly_review import WeeklyInvestorReview


def test_investor_package_service_creates_archive(tmp_path: Path):

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

    output_directory = tmp_path / "exports"

    archive_root = tmp_path / "archive"

    result = InvestorPackageService().create_package(
        review,
        output_directory,
        archive_root,
    )

    assert result.exists()

    assert (
        result / "investor_review.txt"
    ).exists()

    assert (
        result / "investor_review.md"
    ).exists()

    assert (
        result / "investor_review.xlsx"
    ).exists()

    assert (
        result / "metadata.json"
    ).exists()
