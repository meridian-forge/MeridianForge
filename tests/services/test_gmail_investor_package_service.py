from __future__ import annotations

from meridianforge.models.domain.investment_strategy import InvestmentStrategy
from meridianforge.models.domain.investor_profile import InvestorProfile
from meridianforge.services.gmail_investor_package_service import (
    GmailInvestorPackageService,
)
from meridianforge.workflows.email_artifact_extraction_workflow import (
    EmailExtractionArtifact,
    EmailExtractionBatch,
)


def test_generate_gmail_investor_package(tmp_path) -> None:
    service = GmailInvestorPackageService()

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
    assert "MeridianForge Gmail Investor Package" in result.report
