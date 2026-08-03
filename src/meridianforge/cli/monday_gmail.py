from __future__ import annotations

from pathlib import Path

from meridianforge.models.domain.investor_profile import InvestorProfile
from meridianforge.services.monday_gmail_execution_service import (
    MondayGmailExecutionService,
)
from meridianforge.workflows.email_artifact_extraction_workflow import (
    EmailExtractionBatch,
)


class MondayGmailCommand:
    """
    Canonical CLI entry point for the production Gmail Monday workflow.

    SP-480.1
    """

    def __init__(
        self,
        execution: MondayGmailExecutionService | None = None,
    ) -> None:
        self._execution = execution or MondayGmailExecutionService()

    def run(
        self,
        extraction_batch: EmailExtractionBatch,
        investor_profile: InvestorProfile,
        output_directory: Path,
    ) -> str:
        result = self._execution.execute(
            extraction_batch,
            investor_profile,
            output_directory,
        )

        return result.dashboard
