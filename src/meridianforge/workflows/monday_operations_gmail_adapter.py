from __future__ import annotations

from dataclasses import dataclass, field

from meridianforge.workflows.email_artifact_extraction_workflow import (
    EmailExtractionBatch,
)
from meridianforge.workflows.monday_gmail_ingestion_workflow import (
    MondayGmailIngestionWorkflow,
)


@dataclass(frozen=True, slots=True)
class MondayOperationsGmailResult:
    processed_messages: int
    extraction_batches: list[EmailExtractionBatch] = field(default_factory=list)


class MondayOperationsGmailAdapter:
    """
    Adapter layer that allows the existing Monday operations
    orchestration path to consume Gmail messages.
    """

    def __init__(
        self,
        gmail_workflow: MondayGmailIngestionWorkflow | None = None,
    ) -> None:
        self._gmail_workflow = gmail_workflow or MondayGmailIngestionWorkflow()

    def ingest_gmail_messages(
        self,
        gmail_messages: list[dict[str, object]],
    ) -> MondayOperationsGmailResult:
        result = self._gmail_workflow.process_messages(
            gmail_messages,
        )

        return MondayOperationsGmailResult(
            processed_messages=result.processed_messages,
            extraction_batches=result.extraction_batches,
        )
