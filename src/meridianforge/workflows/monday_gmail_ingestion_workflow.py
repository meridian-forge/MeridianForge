from __future__ import annotations

from dataclasses import dataclass, field

from meridianforge.workflows.email_artifact_extraction_workflow import (
    EmailExtractionBatch,
)
from meridianforge.workflows.gmail_extraction_workflow import (
    GmailExtractionWorkflow,
)


@dataclass(frozen=True, slots=True)
class MondayGmailIngestionResult:
    processed_messages: int
    extraction_batches: list[EmailExtractionBatch] = field(default_factory=list)


class MondayGmailIngestionWorkflow:
    """
    Monday operations workflow that converts Gmail messages into
    extraction-ready batches.
    """

    def __init__(
        self,
        gmail_workflow: GmailExtractionWorkflow | None = None,
    ) -> None:
        self._gmail_workflow = gmail_workflow or GmailExtractionWorkflow()

    def process_messages(
        self,
        gmail_messages: list[dict[str, object]],
    ) -> MondayGmailIngestionResult:
        batches: list[EmailExtractionBatch] = []

        for message in gmail_messages:
            batches.append(
                self._gmail_workflow.process_message(
                    message,
                )
            )

        return MondayGmailIngestionResult(
            processed_messages=len(gmail_messages),
            extraction_batches=batches,
        )
