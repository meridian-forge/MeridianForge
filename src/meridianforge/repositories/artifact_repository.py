"""
Artifact repository.

MF-502

Stores discovered MeridianForge artifacts and prevents duplicates.
"""

from __future__ import annotations

import hashlib
from pathlib import Path

from meridianforge.artifacts.artifact_record import (
    ArtifactRecord,
)


class ArtifactRepository:
    """
    In-memory artifact registry.

    Responsible for:
    - storing artifacts
    - duplicate detection
    - artifact lookup
    """

    def __init__(self) -> None:
        self._artifacts: dict[str, ArtifactRecord] = {}

    def register(
        self,
        path: Path,
        source: str,
    ) -> ArtifactRecord:
        """
        Register an artifact.

        Duplicate files return the existing record.
        """

        checksum = self._checksum(path)

        existing = self._artifacts.get(checksum)

        if existing is not None:
            return existing

        artifact = ArtifactRecord(
            path=path,
            metadata={
                "source": source,
                "checksum": checksum,
            },
        )

        self._artifacts[checksum] = artifact

        return artifact

    def add(
        self,
        artifact: ArtifactRecord,
    ) -> ArtifactRecord:
        """
        Add an existing artifact record.
        """

        checksum = artifact.metadata.get(
            "checksum",
            self._checksum(artifact.path),
        )

        artifact.metadata["checksum"] = checksum

        self._artifacts[checksum] = artifact

        return artifact

    def all(
        self,
    ) -> list[ArtifactRecord]:
        """
        Return registered artifacts.
        """

        return list(
            self._artifacts.values(),
        )

    @staticmethod
    def _checksum(
        path: Path,
    ) -> str:
        """
        Generate file checksum.
        """

        digest = hashlib.sha256()

        with path.open(
            "rb",
        ) as file:

            for chunk in iter(
                lambda: file.read(4096),
                b"",
            ):
                digest.update(chunk)

        return digest.hexdigest()
