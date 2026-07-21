"""
Investor package domain models.

Defines the structure of generated investor decision packages.
"""

from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path


@dataclass(slots=True)
class InvestorPackageArtifact:
    """
    Represents an artifact contained in an investor package.
    """

    name: str
    location: Path
    artifact_type: str


@dataclass(slots=True)
class InvestorPackage:
    """
    Represents a complete investor decision package.
    """

    package_id: str
    property_name: str
    recommendation: str
    confidence: float
    created_at: datetime
    executive_summary: str = ""
    artifacts: list[InvestorPackageArtifact] = field(
        default_factory=list,
    )

    def add_artifact(
        self,
        artifact: InvestorPackageArtifact,
    ) -> None:
        """
        Add an artifact to the package.
        """

        self.artifacts.append(
            artifact,
        )
