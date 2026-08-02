from __future__ import annotations

from dataclasses import dataclass, field

from meridianforge.services.email_artifact_repository_service import (
    EmailRepositoryArtifact,
)


@dataclass(frozen=True, slots=True)
class EmailExtractionArtifact:
    artifact_id: str
    filename: str
    source: str
    provider: str | None = None
    metadata: dict[str, str] = field(default_factory=dict)


@dataclass(frozen=True, slots=True)
class EmailExtractionBatch:
    artifacts: list[EmailExtractionArtifact] = field(default_factory=list)


class EmailArtifactExtractionWorkflow:
    """
    Prepare repository-managed email artifacts for the extraction pipeline.
    """

    def build_extraction_batch(
        self,
        artifacts: list[EmailRepositoryArtifact],
    ) -> EmailExtractionBatch:
        extraction_artifacts: list[EmailExtractionArtifact] = []

        for artifact in artifacts:
            extraction_artifacts.append(
                EmailExtractionArtifact(
                    artifact_id=artifact.artifact_id,
                    filename=artifact.filename,
                    source=artifact.source,
                    provider=artifact.metadata.get("sender"),
                    metadata=dict(artifact.metadata),
                )
            )

        return EmailExtractionBatch(
            artifacts=extraction_artifacts,
        )
