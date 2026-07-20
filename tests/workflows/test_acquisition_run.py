from pathlib import Path

from meridianforge.operations.investor_package_service import (
    InvestorPackageService,
)
from meridianforge.product.decision_card import (
    InvestorDecisionCard,
)
from meridianforge.product.weekly_review import (
    WeeklyInvestorReview,
)
from meridianforge.workflows.acquisition_context import (
    AcquisitionRunContext,
)
from meridianforge.workflows.acquisition_input import (
    AcquisitionInput,
)
from meridianforge.workflows.acquisition_run import (
    AcquisitionRunService,
)


def test_acquisition_run_creates_investor_package(tmp_path: Path):

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

    context = AcquisitionRunContext(
        opportunity=AcquisitionInput(
            property_address="123 Main St",
            purchase_price=250000,
            market="Jacksonville",
            source="Zillow",
        ),
        review=review,
    )

    result = AcquisitionRunService(
        InvestorPackageService(),
    ).execute(
        context,
        tmp_path / "exports",
        tmp_path / "archive",
    )

    assert result.recommendation == "BUY"
    assert result.confidence == 0.91
    assert result.package_location.exists()
