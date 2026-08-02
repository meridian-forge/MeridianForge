from __future__ import annotations

from dataclasses import dataclass, field

from meridianforge.workflows.email_artifact_extraction_workflow import (
    EmailExtractionBatch,
)
from meridianforge.workflows.monday_operations_gmail_adapter import (
    MondayOperationsGmailAdapter,
)


@dataclass(frozen=True, slots=True)
class MondayOperationsOrchestratorGmailResult:
    processed_messages: int
    extraction_batches: list[EmailExtractionBatch] = field(default_factory=list)


class MondayOperationsOrchestratorGmail:
    """
    Orchestration entry point that integrates Gmail ingestion into the
    Monday operations execution path while preserving backward compatibility.
    """

    def __init__(
        self,
        gmail_adapter: MondayOperationsGmailAdapter | None = None,
    ) -> None:
        self._gmail_adapter = gmail_adapter or MondayOperationsGmailAdapter()

    def run_gmail_ingestion(
        self,
        gmail_messages: list[dict[str, object]],
    ) -> MondayOperationsOrchestratorGmailResult:
        result = self._gmail_adapter.ingest_gmail_messages(
            gmail_messages,
        )

        return MondayOperationsOrchestratorGmailResult(
            processed_messages=result.processed_messages,
            extraction_batches=result.extraction_batches,
        )
