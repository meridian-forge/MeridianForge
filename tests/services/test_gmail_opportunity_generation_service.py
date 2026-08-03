from __future__ import annotations

from meridianforge.services.gmail_opportunity_generation_service import (
    GmailOpportunityGenerationService,
)
from meridianforge.workflows.email_artifact_extraction_workflow import (
    EmailExtractionArtifact,
    EmailExtractionBatch,
)


def test_generate_gmail_opportunities_from_extraction_batch() -> None:
    service = GmailOpportunityGenerationService()

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

    result = service.generate(batch)

    assert len(result.opportunities) == 2
    assert result.opportunities[0].source == "gmail"
    assert result.opportunities[0].provider == "deals@example.com"
