from meridianforge.models.domain.extraction_audit import (
    ExtractionAuditRecord,
    ExtractionAuditStatus,
)
from meridianforge.repositories.extraction_audit_repository import (
    ExtractionAuditRepository,
)
from meridianforge.services.adaptive_extractor_selector import (
    AdaptiveExtractorSelector,
)
from meridianforge.services.extractor_performance_service import (
    ExtractorPerformanceService,
)


def _record(
    extractor: str,
    status: ExtractionAuditStatus,
) -> ExtractionAuditRecord:
    return ExtractionAuditRecord(
        artifact_id="artifact",
        source_file="deal.pdf",
        field_name="purchase_price",
        raw_value="$300,000",
        normalized_value="300000",
        confidence=0.90,
        extractor=extractor,
        status=status,
    )


def test_selector_prefers_best_historical_extractor() -> None:
    repository = ExtractionAuditRepository()

    repository.save(
        _record(
            "ExtractorA",
            ExtractionAuditStatus.ACCEPTED,
        )
    )

    repository.save(
        _record(
            "ExtractorA",
            ExtractionAuditStatus.ACCEPTED,
        )
    )

    repository.save(
        _record(
            "ExtractorB",
            ExtractionAuditStatus.REVIEW,
        )
    )

    service = ExtractorPerformanceService(
        repository=repository,
    )

    selector = AdaptiveExtractorSelector(
        performance_service=service,
    )

    assert (
        selector.select(
            [
                "ExtractorA",
                "ExtractorB",
            ]
        )
        == "ExtractorA"
    )


def test_selector_falls_back_when_no_history_exists() -> None:
    selector = AdaptiveExtractorSelector()

    assert (
        selector.select(
            [
                "ExtractorA",
                "ExtractorB",
            ]
        )
        == "ExtractorA"
    )

    assert (
        selector.select(
            [],
        )
        is None
    )


def test_selector_prefers_provider_learning_over_generic_performance() -> None:
    from meridianforge.models.domain.extractor_learning_profile import (
        ExtractorLearningProfile,
    )

    class LearningServiceStub:
        def get_profiles(
            self,
            provider: str | None = None,
        ) -> list[ExtractorLearningProfile]:
            return [
                ExtractorLearningProfile(
                    extractor="ExtractorB",
                    provider="JWB Capital",
                    average_confidence=0.99,
                    total_records=5,
                ),
            ]

    repository = ExtractionAuditRepository()

    repository.save(
        _record(
            "ExtractorA",
            ExtractionAuditStatus.ACCEPTED,
        )
    )

    selector = AdaptiveExtractorSelector(
        performance_service=ExtractorPerformanceService(
            repository=repository,
        ),
        learning_service=LearningServiceStub(),
    )

    assert (
        selector.select(
            [
                "ExtractorA",
                "ExtractorB",
            ],
            provider="JWB Capital",
        )
        == "ExtractorB"
    )
