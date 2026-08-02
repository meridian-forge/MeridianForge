from meridianforge.models.domain.extraction_audit import (
    ExtractionAuditRecord,
    ExtractionAuditStatus,
)
from meridianforge.repositories.extraction_audit_repository import (
    ExtractionAuditRepository,
)
from meridianforge.services.extractor_learning_service import (
    ExtractorLearningService,
)


def test_extractor_learning_builds_profile() -> None:
    repository = ExtractionAuditRepository()

    repository.save(
        ExtractionAuditRecord(
            artifact_id="artifact-1",
            source_file="deal.pdf",
            field_name="purchase_price",
            raw_value="$339000",
            normalized_value="339000",
            confidence=0.98,
            extractor="RentalAcquisitionExtractor",
            status=ExtractionAuditStatus.ACCEPTED,
        )
    )

    repository.save(
        ExtractionAuditRecord(
            artifact_id="artifact-1",
            source_file="deal.pdf",
            field_name="taxes",
            raw_value="unknown",
            normalized_value=None,
            confidence=0.20,
            extractor="RentalAcquisitionExtractor",
            status=ExtractionAuditStatus.REJECTED,
        )
    )

    service = ExtractorLearningService(
        repository=repository,
    )

    profiles = service.build_profiles()

    assert len(profiles) == 1
    assert profiles[0].extractor == "RentalAcquisitionExtractor"
    assert "purchase_price" in profiles[0].successful_fields
    assert "taxes" in profiles[0].failed_fields
    assert profiles[0].total_records == 2


def test_extractor_learning_separates_profiles_by_provider() -> None:
    repository = ExtractionAuditRepository()

    repository.save(
        ExtractionAuditRecord(
            artifact_id="artifact-1",
            source_file="jwb.pdf",
            field_name="purchase_price",
            raw_value="$339000",
            normalized_value="339000",
            confidence=0.98,
            extractor="RentalAcquisitionExtractor",
            status=ExtractionAuditStatus.ACCEPTED,
            provider="JWB Capital",
        )
    )

    repository.save(
        ExtractionAuditRecord(
            artifact_id="artifact-2",
            source_file="other.pdf",
            field_name="purchase_price",
            raw_value="$339000",
            normalized_value="339000",
            confidence=0.98,
            extractor="RentalAcquisitionExtractor",
            status=ExtractionAuditStatus.ACCEPTED,
            provider="Other Provider",
        )
    )

    profiles = ExtractorLearningService(
        repository=repository,
    ).build_profiles()

    assert len(profiles) == 2

    providers = {profile.provider for profile in profiles}

    assert providers == {
        "JWB Capital",
        "Other Provider",
    }
