from meridianforge.models.opportunity import OpportunityType
from meridianforge.services.opportunity_router import (
    OpportunityRouter,
)


class ProviderAwareSelectorStub:
    def __init__(self) -> None:
        self.provider: str | None = None

    def select(
        self,
        candidates: list[str],
        provider: str | None = None,
    ) -> str:
        self.provider = provider

        return candidates[-1]


def test_router_passes_provider_into_selector() -> None:
    selector = ProviderAwareSelectorStub()

    router = OpportunityRouter(
        selector=selector,
    )

    context = router.route_with_context(
        OpportunityType.RENTAL_ACQUISITION,
        provider="JWB Capital",
    )

    assert selector.provider == "JWB Capital"
    assert context.provider == "JWB Capital"
    assert context.selected_extractor == "AlternativeRentalExtractor"
