from pathlib import Path

from meridianforge.models.opportunity import (
    OpportunityClassification,
    OpportunityType,
)
from meridianforge.services.monday_operations_orchestrator import (
    MondayOperationsOrchestrator,
)
from meridianforge.services.opportunity_intake_service import (
    IntakeArtifact,
    OpportunityIntakeService,
)


class RentalTestIntakeService(OpportunityIntakeService):
    def ingest_directory(
        self,
        directory: Path,
    ) -> list[IntakeArtifact]:
        return [
            IntakeArtifact(
                path=directory / "deal.pdf",
                classification=OpportunityClassification(
                    opportunity_type=OpportunityType.RENTAL_ACQUISITION,
                    confidence=0.99,
                    reason="Test rental opportunity",
                ),
                extracted_text=(
                    "Location: Rosharon, TX\n"
                    "Price: $339,000\n"
                    "Rent: $3,135\n"
                    "Cashflow: $539\n"
                    "ROI: 8.7%\n"
                ),
            )
        ]


def test_monday_operations_orchestrator_processes_inbox(
    tmp_path: Path,
) -> None:
    inbox = tmp_path / "inbox"
    inbox.mkdir()

    orchestrator = MondayOperationsOrchestrator(
        intake=RentalTestIntakeService(),
    )

    result = orchestrator.execute(
        inbox,
    )

    assert result.artifacts_processed == 1
    assert len(result.routed_extractors) == 1
    assert result.routed_extractors[0] == "RentalAcquisitionExtractor"

    assert len(result.extractor_decisions) == 1
    assert (
        result.extractor_decisions[0].selected_extractor == "RentalAcquisitionExtractor"
    )

    assert len(result.normalized_opportunities) == 1
    assert result.normalized_opportunities[0].city == "Rosharon"
    assert "Extraction Audit Dashboard" in result.audit_report
