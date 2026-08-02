"""
Monday operations orchestrator.

SP-430.1 / SP-430.4.1 / MF-440.3

Coordinates the Monday operating workflow by connecting opportunity
intake, adaptive routing, extraction execution, normalization, and
extraction audit reporting into a single execution boundary.

MF-440.3 exposes extractor decision intelligence through the Monday
workflow while preserving existing operational behavior.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from meridianforge.models.domain.extractor_decision_context import (
    ExtractorDecisionContext,
)
from meridianforge.reporting.extraction_audit_report import (
    ExtractionAuditReport,
)
from meridianforge.services.extraction_pipeline_service import (
    ExtractionPipelineService,
)
from meridianforge.services.opportunity_intake_service import (
    OpportunityIntakeService,
)
from meridianforge.services.opportunity_mapper import (
    NormalizedRentalOpportunity,
)
from meridianforge.services.opportunity_router import (
    OpportunityRouter,
)


@dataclass(frozen=True, slots=True)
class MondayOperationsResult:
    """
    Result of a Monday operations execution.
    """

    artifacts_processed: int
    routed_extractors: list[str]
    extractor_decisions: list[ExtractorDecisionContext]
    normalized_opportunities: list[NormalizedRentalOpportunity]
    audit_report: str


class MondayOperationsOrchestrator:
    """
    Execute the Monday intake, routing, extraction, and normalization workflow.
    """

    def __init__(
        self,
        intake: OpportunityIntakeService | None = None,
        router: OpportunityRouter | None = None,
        extraction_pipeline: ExtractionPipelineService | None = None,
        audit_report: ExtractionAuditReport | None = None,
    ) -> None:
        self._intake = intake or OpportunityIntakeService()
        self._router = router or OpportunityRouter()
        self._pipeline = extraction_pipeline or ExtractionPipelineService()
        self._audit_report = audit_report or ExtractionAuditReport()

    def execute(
        self,
        inbox: Path,
    ) -> MondayOperationsResult:
        """
        Process an inbox directory through intake, routing, extraction,
        and normalization.
        """

        artifacts = self._intake.ingest_directory(
            inbox,
        )

        routed_extractors: list[str] = []
        extractor_decisions: list[ExtractorDecisionContext] = []
        normalized_opportunities: list[NormalizedRentalOpportunity] = []

        for artifact in artifacts:
            decision = self._router.route_with_context(
                artifact.classification.opportunity_type,
            )

            routed_extractors.append(
                decision.selected_extractor,
            )

            extractor_decisions.append(
                decision,
            )

            opportunity = self._pipeline.process(
                artifact=artifact,
                decision_context=decision,
            )

            if opportunity is not None:
                normalized_opportunities.append(
                    opportunity,
                )

        report = self._audit_report.generate()

        return MondayOperationsResult(
            artifacts_processed=len(artifacts),
            routed_extractors=routed_extractors,
            extractor_decisions=extractor_decisions,
            normalized_opportunities=normalized_opportunities,
            audit_report=report,
        )
