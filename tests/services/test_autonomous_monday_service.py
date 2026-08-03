from __future__ import annotations

from meridianforge.models.domain.investment_strategy import InvestmentStrategy
from meridianforge.models.domain.investor_profile import InvestorProfile
from meridianforge.services.autonomous_monday_service import (
    AutonomousMondayService,
)
from meridianforge.services.gmail_execution_ledger_service import (
    GmailExecutionLedgerService,
)
from meridianforge.workflows.email_artifact_extraction_workflow import (
    EmailExtractionArtifact,
    EmailExtractionBatch,
)


def test_execute_autonomous_monday_loop(tmp_path) -> None:
    ledger = GmailExecutionLedgerService(tmp_path / "gmail_execution_ledger.txt")

    service = AutonomousMondayService(
        ledger=ledger,
    )

    batch = EmailExtractionBatch(
        artifacts=[
            EmailExtractionArtifact(
                artifact_id="gmail-1",
                filename="deal.pdf",
                source="email",
                provider="deals@example.com",
            ),
            EmailExtractionArtifact(
                artifact_id="gmail-1",
                filename="deal.pdf",
                source="email",
                provider="deals@example.com",
            ),
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

    assert result.processed_messages == 1
    assert result.skipped_messages == 1
    assert result.package_location is not None
    assert result.package_location.exists()
