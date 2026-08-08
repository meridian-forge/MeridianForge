"""
Monday operations orchestrator.

SP-430.1 / SP-430.4.1 / MF-460.1 / SP-490.2

Coordinates the Monday operating workflow by connecting opportunity
intake, adaptive routing, extraction execution, normalization, and
evidence-based underwriting into a single execution boundary.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from meridianforge.models.domain.extractor_decision_context import (
    ExtractorDecisionContext,
)
from meridianforge.models.domain.investment_strategy import (
    InvestmentStrategy,
)
from meridianforge.models.domain.investor_profile import (
    InvestorProfile,
)
from meridianforge.reporting.extraction_audit_report import (
    ExtractionAuditReport,
)
from meridianforge.services.extraction_pipeline_service import (
    ExtractionPipelineService,
)
from meridianforge.services.monday_evidence_service import (
    MondayEvidenceService,
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
from meridianforge.workflows.monday_operations_gmail_adapter import (
    MondayOperationsGmailAdapter,
)


@dataclass(frozen=True, slots=True)
class MondayOperationsResult:
    artifacts_processed: int
    routed_extractors: list[str]
    extractor_decisions: list[ExtractorDecisionContext]
    normalized_opportunities: list[NormalizedRentalOpportunity]
    audit_report: str


class MondayOperationsOrchestrator:
    """
    Execute the Monday intake, routing, extraction, normalization,
    and evidence-underwriting workflow.
    """

    IMAGE_SUFFIXES = {
        ".png",
        ".jpg",
        ".jpeg",
        ".webp",
    }

    def __init__(
        self,
        intake: OpportunityIntakeService | None = None,
        router: OpportunityRouter | None = None,
        extraction_pipeline: ExtractionPipelineService | None = None,
        audit_report: ExtractionAuditReport | None = None,
        gmail_adapter: MondayOperationsGmailAdapter | None = None,
        evidence: MondayEvidenceService | None = None,
    ) -> None:
        self._intake = intake or OpportunityIntakeService()
        self._router = router or OpportunityRouter()
        self._pipeline = extraction_pipeline or ExtractionPipelineService()
        self._audit_report = audit_report or ExtractionAuditReport()
        self._gmail_adapter = gmail_adapter or MondayOperationsGmailAdapter()
        self._evidence = evidence or MondayEvidenceService()

    def execute(
        self,
        inbox: Path,
    ) -> MondayOperationsResult:
        artifacts = self._intake.ingest_directory(inbox)

        routed_extractors: list[str] = []
        extractor_decisions: list[ExtractorDecisionContext] = []
        normalized_opportunities: list[NormalizedRentalOpportunity] = []

        investor_profile = InvestorProfile(
            name="Monday Operations",
            strategy=list(InvestmentStrategy)[0],
        )

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

            artifact_path = Path(artifact.path)

            if artifact_path.suffix.lower() in self.IMAGE_SUFFIXES:
                try:
                    self._evidence.analyze_artifact(
                        artifact_path,
                        investor_profile,
                    )
                except Exception:
                    pass

        report = self._audit_report.generate()

        return MondayOperationsResult(
            artifacts_processed=len(artifacts),
            routed_extractors=routed_extractors,
            extractor_decisions=extractor_decisions,
            normalized_opportunities=normalized_opportunities,
            audit_report=report,
        )

    def execute_gmail_messages(
        self,
        gmail_messages: list[dict[str, object]],
    ) -> MondayOperationsResult:
        gmail_result = self._gmail_adapter.ingest_gmail_messages(
            gmail_messages,
        )

        report = self._audit_report.generate()

        return MondayOperationsResult(
            artifacts_processed=gmail_result.processed_messages,
            routed_extractors=[],
            extractor_decisions=[],
            normalized_opportunities=[],
            audit_report=report,
        )
