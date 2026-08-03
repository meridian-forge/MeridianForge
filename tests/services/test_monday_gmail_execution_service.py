from __future__ import annotations

from meridianforge.models.domain.investment_strategy import InvestmentStrategy
from meridianforge.models.domain.investor_profile import InvestorProfile
from meridianforge.services.monday_gmail_execution_service import (
    MondayGmailExecutionService,
)
from meridianforge.workflows.email_artifact_extraction_workflow import (
    EmailExtractionArtifact,
    EmailExtractionBatch,
)


def test_execute_monday_gmail_workflow(tmp_path) -> None:
    service = MondayGmailExecutionService()

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
        tmp_path,
    )

    assert result.analyzed_opportunities == 1
    assert result.package_location.exists()
    assert "MeridianForge Monday Gmail Execution" in result.dashboard
