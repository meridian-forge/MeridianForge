from __future__ import annotations

from meridianforge.workflows.email_artifact_extraction_workflow import (
    EmailArtifactExtractionWorkflow,
    EmailExtractionBatch,
)
from meridianforge.workflows.gmail_artifact_repository_workflow import (
    GmailArtifactRepositoryWorkflow,
)


class GmailExtractionWorkflow:
    """
    End-to-end workflow from Gmail connector message to
    extraction-ready email artifacts.
    """

    def __init__(
        self,
        repository_workflow: GmailArtifactRepositoryWorkflow | None = None,
        extraction_workflow: EmailArtifactExtractionWorkflow | None = None,
    ) -> None:
        self._repository_workflow = (
            repository_workflow or GmailArtifactRepositoryWorkflow()
        )
        self._extraction_workflow = (
            extraction_workflow or EmailArtifactExtractionWorkflow()
        )

    def process_message(
        self,
        gmail_message: dict[str, object],
    ) -> EmailExtractionBatch:
        repository_artifacts = self._repository_workflow.process_message(
            gmail_message,
        )

        return self._extraction_workflow.build_extraction_batch(
            repository_artifacts,
        )
