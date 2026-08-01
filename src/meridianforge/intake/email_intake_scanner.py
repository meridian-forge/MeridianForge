from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from meridianforge.artifacts.artifact_classifier import (
    ArtifactClassifier,
    ArtifactType,
)


@dataclass(slots=True)
class EmailArtifact:
    path: Path
    artifact_type: ArtifactType


@dataclass(slots=True)
class EmailIntakeResult:
    artifacts: list[EmailArtifact]

    @property
    def total_files(self) -> int:
        return len(self.artifacts)


class EmailIntakeScanner:
    """
    MF-507.2

    Scans a simulated email inbox directory and classifies incoming
    artifacts for downstream routing.
    """

    def __init__(
        self,
        classifier: ArtifactClassifier | None = None,
    ) -> None:
        self.classifier = classifier or ArtifactClassifier()

    def scan(
        self,
        inbox_directory: Path,
    ) -> EmailIntakeResult:
        if not inbox_directory.exists():
            return EmailIntakeResult(
                artifacts=[],
            )

        artifacts: list[EmailArtifact] = []

        for path in sorted(inbox_directory.iterdir()):
            if not path.is_file():
                continue

            artifacts.append(
                EmailArtifact(
                    path=path,
                    artifact_type=self.classifier.classify(path),
                )
            )

        return EmailIntakeResult(
            artifacts=artifacts,
        )
