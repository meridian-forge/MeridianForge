from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from meridianforge.models.domain.investor_profile import InvestorProfile
from meridianforge.services.gmail_execution_ledger_service import (
    GmailExecutionLedgerService,
)
from meridianforge.services.monday_gmail_execution_service import (
    MondayGmailExecutionResult,
    MondayGmailExecutionService,
)
from meridianforge.workflows.email_artifact_extraction_workflow import (
    EmailExtractionArtifact,
    EmailExtractionBatch,
)


@dataclass(frozen=True, slots=True)
class AutonomousMondayResult:
    processed_messages: int
    skipped_messages: int
    dashboard: str
    package_location: Path | None


class AutonomousMondayService:
    """
    Execute the autonomous Monday operating loop.

    SP-480.5
    """

    def __init__(
        self,
        execution: MondayGmailExecutionService | None = None,
        ledger: GmailExecutionLedgerService | None = None,
    ) -> None:
        self._execution = execution or MondayGmailExecutionService()
        self._ledger = ledger

    def execute(
        self,
        extraction_batch: EmailExtractionBatch,
        investor_profile: InvestorProfile,
        output_directory: Path,
    ) -> AutonomousMondayResult:
        fresh_artifacts: list[EmailExtractionArtifact] = []
        skipped = 0

        for artifact in extraction_batch.artifacts:
            if self._ledger is not None:
                if self._ledger.already_processed(artifact.artifact_id):
                    skipped += 1
                    continue

                self._ledger.mark_processed(artifact.artifact_id)

            fresh_artifacts.append(artifact)

        if not fresh_artifacts:
            return AutonomousMondayResult(
                processed_messages=0,
                skipped_messages=skipped,
                dashboard="# MeridianForge Monday\\n\\nNo new Gmail opportunities.",
                package_location=None,
            )

        execution_result: MondayGmailExecutionResult = self._execution.execute(
            EmailExtractionBatch(artifacts=fresh_artifacts),
            investor_profile,
            output_directory,
        )

        return AutonomousMondayResult(
            processed_messages=len(fresh_artifacts),
            skipped_messages=skipped,
            dashboard=execution_result.dashboard,
            package_location=execution_result.package_location,
        )
