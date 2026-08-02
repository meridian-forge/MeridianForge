from meridianforge.models.domain.extraction_audit import (
    ExtractionAuditRecord,
    ExtractionAuditStatus,
)
from meridianforge.models.opportunity import OpportunityType
from meridianforge.repositories.extraction_audit_repository import (
    ExtractionAuditRepository,
)
from meridianforge.services.adaptive_extractor_selector import (
    AdaptiveExtractorSelector,
)
from meridianforge.services.extractor_performance_service import (
    ExtractorPerformanceService,
)
from meridianforge.services.opportunity_router import OpportunityRouter


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
        confidence=0.95,
        extractor=extractor,
        status=status,
    )


def test_router_prefers_best_rental_extractor() -> None:
    repository = ExtractionAuditRepository()

    repository.save(
        _record(
            "AlternativeRentalExtractor",
            ExtractionAuditStatus.ACCEPTED,
        )
    )

    repository.save(
        _record(
            "AlternativeRentalExtractor",
            ExtractionAuditStatus.ACCEPTED,
        )
    )

    repository.save(
        _record(
            "RentalAcquisitionExtractor",
            ExtractionAuditStatus.REVIEW,
        )
    )

    performance = ExtractorPerformanceService(
        repository=repository,
    )

    selector = AdaptiveExtractorSelector(
        performance_service=performance,
    )

    router = OpportunityRouter(
        selector=selector,
    )

    assert (
        router.route(
            OpportunityType.RENTAL_ACQUISITION,
        )
        == "AlternativeRentalExtractor"
    )


def test_router_falls_back_for_non_adaptive_types() -> None:
    router = OpportunityRouter()

    assert (
        router.route(
            OpportunityType.PRIVATE_LENDING,
        )
        == "PrivateLendingExtractor"
    )

    assert (
        router.route(
            OpportunityType.INVENTORY_WORKBOOK,
        )
        == "InventoryWorkbookExtractor"
    )
