from pathlib import Path

from meridianforge.product.decision_card import (
    InvestorDecisionCard,
)
from meridianforge.product.weekly_review import (
    WeeklyInvestorReview,
)
from meridianforge.services.monday_artifact_service import (
    MondayArtifactService,
)


def test_monday_artifact_generation(
    tmp_path: Path,
):

    review = WeeklyInvestorReview(
        cards=[
            InvestorDecisionCard(
                rank=1,
                property_address="123 Main St",
                recommendation="BUY",
                confidence=0.90,
                strengths=["Cash flow positive"],
                risks=["Older roof"],
            )
        ]
    )

    output = MondayArtifactService().generate(
        review,
        tmp_path,
    )

    assert (output / "Dashboard.txt").exists()

    assert (output / "Dashboard.json").exists()

    assert (output / "BUY").exists()
