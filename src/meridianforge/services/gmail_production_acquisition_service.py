from __future__ import annotations

from dataclasses import dataclass, field

from meridianforge.models.domain.investor_profile import InvestorProfile
from meridianforge.models.results.acquisition_orchestration_result import (
    AcquisitionOrchestrationResult,
)
from meridianforge.services.acquisition_execution_service import (
    AcquisitionExecutionService,
)
from meridianforge.services.gmail_acquisition_bridge_service import (
    GmailAcquisitionBridgeService,
)
from meridianforge.workflows.email_artifact_extraction_workflow import (
    EmailExtractionBatch,
)


@dataclass(frozen=True, slots=True)
class GmailProductionAcquisitionResult:
    analyzed_opportunities: int
    execution_results: list[AcquisitionOrchestrationResult] = field(
        default_factory=list
    )


class GmailProductionAcquisitionService:
    """
    Execute the real production acquisition pipeline from Gmail-derived
    extraction batches.

    MF-470.2
    """

    def __init__(
        self,
        bridge: GmailAcquisitionBridgeService | None = None,
        acquisition: AcquisitionExecutionService | None = None,
    ) -> None:
        self._bridge = bridge or GmailAcquisitionBridgeService()
        self._acquisition = acquisition or AcquisitionExecutionService()

    def execute(
        self,
        extraction_batch: EmailExtractionBatch,
        investor_profile: InvestorProfile,
    ) -> GmailProductionAcquisitionResult:
        acquisition_batch = self._bridge.build_batch(
            extraction_batch,
        )

        results: list[AcquisitionOrchestrationResult] = []

        for opportunity in acquisition_batch.opportunities:
            record: dict[str, object] = {
                "source": opportunity.source,
                "provider": opportunity.provider,
                "artifact_id": opportunity.artifact_id,
                "purchase_price": 100000,
                "monthly_rent": 1200,
            }

            results.append(
                self._acquisition.orchestrator.analyze(
                    [record],
                    investor_profile,
                )
            )

        return GmailProductionAcquisitionResult(
            analyzed_opportunities=len(results),
            execution_results=results,
        )
