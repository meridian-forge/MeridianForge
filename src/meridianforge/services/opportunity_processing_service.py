"""
Opportunity processing service.

MF-512.4.1

Bridges artifact intake, routing, extraction,
normalization, and acquisition execution.

Production Monday ingestion path.
"""

from __future__ import annotations

from pathlib import Path

from meridianforge.models.domain.investor_profile import (
    InvestorProfile,
)
from meridianforge.models.results.acquisition_orchestration_result import (
    AcquisitionOrchestrationResult,
)
from meridianforge.services.acquisition_execution_service import (
    AcquisitionExecutionService,
)
from meridianforge.services.extraction_pipeline_service import (
    ExtractionPipelineService,
)
from meridianforge.services.opportunity_intake_service import (
    OpportunityIntakeService,
)
from meridianforge.services.opportunity_router import (
    OpportunityRouter,
)


class OpportunityProcessingService:
    """
    Execute the production opportunity ingestion pipeline.
    """

    def __init__(
        self,
        intake: OpportunityIntakeService | None = None,
        router: OpportunityRouter | None = None,
        extraction: ExtractionPipelineService | None = None,
        execution: AcquisitionExecutionService | None = None,
    ) -> None:

        self.intake = intake or OpportunityIntakeService()
        self.router = router or OpportunityRouter()
        self.extraction = extraction or ExtractionPipelineService()
        self.execution = execution or AcquisitionExecutionService()

    def process_artifact(
        self,
        path: Path,
        investor_profile: InvestorProfile,
    ) -> AcquisitionOrchestrationResult | None:
        """
        Process a single artifact.
        """

        artifact = self.intake.ingest_file(path)

        context = self.router.route_with_context(
            artifact.classification.opportunity_type,
        )

        normalized = self.extraction.process(
            artifact,
            decision_context=context,
        )

        if normalized is None:
            return None

        if isinstance(normalized, list):
            first_review = None

            for opportunity in normalized:
                try:
                    result = self.execution.execute(
                        opportunity,
                        investor_profile,
                    )

                    if first_review is None:
                        first_review = result

                except Exception:
                    continue

            return first_review

        return self.execution.execute(
            normalized,
            investor_profile,
        )

    def process_artifacts(
        self,
        paths: list[Path],
        investor_profile: InvestorProfile,
    ) -> list[AcquisitionOrchestrationResult]:
        """
        Process multiple artifacts.
        """

        results: list[AcquisitionOrchestrationResult] = []

        for path in paths:
            try:
                result = self.process_artifact(
                    path,
                    investor_profile,
                )

                if result is not None:
                    results.append(result)

            except Exception:
                continue

        return results
