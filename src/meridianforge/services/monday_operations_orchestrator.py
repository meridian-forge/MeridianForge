"""
Monday operations orchestrator.

SP-430.1

Coordinates the Monday operating workflow by connecting opportunity
intake, adaptive routing, and extraction audit reporting into a single
execution boundary.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from meridianforge.reporting.extraction_audit_report import (
    ExtractionAuditReport,
)
from meridianforge.services.opportunity_intake_service import (
    OpportunityIntakeService,
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
    audit_report: str


class MondayOperationsOrchestrator:
    """
    Execute the Monday intake and routing workflow.
    """

    def __init__(
        self,
        intake: OpportunityIntakeService | None = None,
        router: OpportunityRouter | None = None,
        audit_report: ExtractionAuditReport | None = None,
    ) -> None:
        self._intake = intake or OpportunityIntakeService()
        self._router = router or OpportunityRouter()
        self._audit_report = audit_report or ExtractionAuditReport()

    def execute(
        self,
        inbox: Path,
    ) -> MondayOperationsResult:
        """
        Process an inbox directory through intake and routing.
        """

        artifacts = self._intake.ingest_directory(
            inbox,
        )

        routed_extractors = [
            self._router.route(
                artifact.classification.opportunity_type,
            )
            for artifact in artifacts
        ]

        report = self._audit_report.generate()

        return MondayOperationsResult(
            artifacts_processed=len(artifacts),
            routed_extractors=routed_extractors,
            audit_report=report,
        )
