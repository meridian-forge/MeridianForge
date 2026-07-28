"""
Artifact lifecycle management.

MF-430.4

Owns artifact state transitions.
"""

from pathlib import Path

from meridianforge.artifacts.artifact_record import (
    ArtifactRecord,
)
from meridianforge.artifacts.artifact_status import (
    ArtifactStatus,
)


class ArtifactLifecycleService:
    """
    Controls artifact movement through
    MeridianForge processing states.
    """

    def register(
        self,
        path: Path,
    ) -> ArtifactRecord:
        """
        Register new incoming artifact.
        """

        return ArtifactRecord(
            path=path,
            status=ArtifactStatus.RECEIVED,
        )

    def validate(
        self,
        artifact: ArtifactRecord,
    ) -> ArtifactRecord:
        """
        Validate artifact existence.
        """

        artifact.status = ArtifactStatus.VALIDATING

        if artifact.path.exists():
            artifact.status = ArtifactStatus.READY

        else:
            artifact.status = ArtifactStatus.REJECTED

            artifact.error = "Artifact file does not exist"

        return artifact

    def mark_analyzed(
        self,
        artifact: ArtifactRecord,
    ) -> ArtifactRecord:
        """
        Mark artifact analysis complete.
        """

        artifact.status = ArtifactStatus.ANALYZED

        return artifact

    def archive(
        self,
        artifact: ArtifactRecord,
    ) -> ArtifactRecord:
        """
        Mark artifact archived.
        """

        artifact.status = ArtifactStatus.ARCHIVED

        return artifact
