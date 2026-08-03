from __future__ import annotations

from meridianforge.cli.monday_gmail import MondayGmailCommand
from meridianforge.models.domain.investment_strategy import InvestmentStrategy
from meridianforge.models.domain.investor_profile import InvestorProfile
from meridianforge.workflows.email_artifact_extraction_workflow import (
    EmailExtractionArtifact,
    EmailExtractionBatch,
)


def test_run_production_monday_gmail_command(tmp_path) -> None:
    command = MondayGmailCommand()

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

    dashboard = command.run(
        batch,
        profile,
        tmp_path,
    )

    assert "MeridianForge Monday Gmail Execution" in dashboard
