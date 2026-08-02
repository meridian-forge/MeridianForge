from __future__ import annotations

from meridianforge.services.gmail_acquisition_execution_service import (
    GmailAcquisitionExecutionService,
)
from meridianforge.workflows.email_artifact_extraction_workflow import (
    EmailExtractionArtifact,
    EmailExtractionBatch,
)


def test_execute_gmail_acquisition_batch() -> None:
    service = GmailAcquisitionExecutionService()

    batch = EmailExtractionBatch(
        artifacts=[
            EmailExtractionArtifact(
                artifact_id="email:gmail-123:deal.pdf",
                filename="deal.pdf",
                source="email",
                provider="deals@example.com",
            ),
            EmailExtractionArtifact(
                artifact_id="email:gmail-123:rent_roll.xlsx",
                filename="rent_roll.xlsx",
                source="email",
                provider="deals@example.com",
            ),
        ]
    )

    result = service.execute(batch)

    assert result.analyzed_opportunities == 2
    assert result.source == "gmail"
