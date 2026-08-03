from __future__ import annotations

from meridianforge.models.domain.investment_strategy import InvestmentStrategy
from meridianforge.models.domain.investor_profile import InvestorProfile
from meridianforge.services.gmail_production_acquisition_service import (
    GmailProductionAcquisitionService,
)
from meridianforge.workflows.email_artifact_extraction_workflow import (
    EmailExtractionArtifact,
    EmailExtractionBatch,
)


def test_execute_gmail_batch_through_real_underwriting_boundary() -> None:
    service = GmailProductionAcquisitionService()

    batch = EmailExtractionBatch(
        artifacts=[
            EmailExtractionArtifact(
                artifact_id="email:gmail-123:deal.pdf",
                filename="deal.pdf",
                source="email",
                provider="deals@example.com",
            )
        ]
    )

    profile = InvestorProfile(
        name="MeridianForge Test Investor",
        strategy=InvestmentStrategy.CASH_FLOW,
    )

    result = service.execute(
        batch,
        profile,
    )

    assert result.analyzed_opportunities == 1
    assert len(result.execution_results) == 1

    orchestration = result.execution_results[0]

    # Validate the production acquisition boundary produced an investor review.
    assert orchestration.review.cards
    assert orchestration.review.cards[0].recommendation
