"""
Artifact lifecycle record.

MF-430.4
"""

from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from uuid import uuid4

from meridianforge.artifacts.artifact_status import (
    ArtifactStatus,
)


@dataclass(slots=True)
class ArtifactRecord:
    """
    Represents an investment artifact
    moving through MeridianForge.
    """

    path: Path

    artifact_id: str = field(default_factory=lambda: str(uuid4()))

    status: ArtifactStatus = ArtifactStatus.RECEIVED

    created_at: datetime = field(default_factory=datetime.now)

    metadata: dict[str, str] = field(default_factory=dict)

    error: str | None = None
