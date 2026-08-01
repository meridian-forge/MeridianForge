from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


@dataclass(slots=True)
class QuarantinedArtifact:
    path: Path
    reason: str
    source: str
    checksum: str
    quarantined_at: datetime


class QuarantineRepository:
    """
    MF-507.4

    Stores artifacts that could not be processed safely by the Monday
    operating loop.
    """

    def __init__(self) -> None:
        self._artifacts: dict[str, QuarantinedArtifact] = {}

    def add(
        self,
        path: Path,
        *,
        reason: str,
        source: str,
        checksum: str,
    ) -> QuarantinedArtifact:
        existing = self._artifacts.get(checksum)
        if existing is not None:
            return existing

        artifact = QuarantinedArtifact(
            path=path,
            reason=reason,
            source=source,
            checksum=checksum,
            quarantined_at=datetime.utcnow(),
        )

        self._artifacts[checksum] = artifact
        return artifact

    def all(self) -> list[QuarantinedArtifact]:
        return list(self._artifacts.values())

    def count(self) -> int:
        return len(self._artifacts)
