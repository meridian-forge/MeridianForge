from pathlib import Path

from meridianforge.models.opportunity import (
    OpportunityClassification,
    OpportunityType,
)
from meridianforge.services.extraction_pipeline_service import (
    ExtractionPipelineService,
)
from meridianforge.services.opportunity_intake_service import (
    IntakeArtifact,
)


def test_extraction_pipeline_normalizes_rental_opportunity(
    tmp_path: Path,
) -> None:
    artifact = IntakeArtifact(
        path=tmp_path / "deal.pdf",
        classification=OpportunityClassification(
            opportunity_type=OpportunityType.RENTAL_ACQUISITION,
            confidence=0.99,
            reason="Rental acquisition document",
        ),
        extracted_text=(
            "Location: Rosharon, TX\n"
            "Price: $339,000\n"
            "Rent: $3,135\n"
            "Cashflow: $539\n"
            "ROI: 8.7%\n"
        ),
    )

    service = ExtractionPipelineService()

    result = service.process(
        artifact=artifact,
        extractor_name="RentalAcquisitionExtractor",
    )

    assert result is not None
    assert result.city == "Rosharon"
    assert result.state == "TX"
    assert result.monthly_rent == 3135


def test_pipeline_accepts_extractor_decision_context(
    tmp_path: Path,
) -> None:
    from meridianforge.models.domain.extractor_decision_context import (
        ExtractorDecisionContext,
    )

    artifact = IntakeArtifact(
        path=tmp_path / "deal.pdf",
        classification=OpportunityClassification(
            opportunity_type=OpportunityType.RENTAL_ACQUISITION,
            confidence=0.99,
            reason="Rental acquisition document",
        ),
        extracted_text=(
            "Location: Rosharon, TX\n"
            "Price: $339,000\n"
            "Rent: $3,135\n"
            "Cashflow: $539\n"
            "ROI: 8.7%\n"
        ),
    )

    context = ExtractorDecisionContext(
        opportunity_type="rental_acquisition",
        selected_extractor="RentalAcquisitionExtractor",
        candidate_extractors=[
            "RentalAcquisitionExtractor",
            "AlternativeRentalExtractor",
        ],
    )

    service = ExtractionPipelineService()

    result = service.process(
        artifact=artifact,
        decision_context=context,
    )

    assert result is not None
    assert result.city == "Rosharon"
