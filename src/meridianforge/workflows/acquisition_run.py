"""
Acquisition workflow orchestration.

Coordinates analysis and investor package creation.
"""

from dataclasses import dataclass
from pathlib import Path
from meridianforge.workflows.acquisition_context import (
    AcquisitionRunContext,
)

@dataclass(slots=True)
class AcquisitionRunResult:
    """
    Result of a complete acquisition workflow run.
    """

    recommendation: str
    confidence: float
    package_location: Path

class AcquisitionRunService:
    """
    Execute a complete acquisition workflow.
    """

    def __init__(
        self,
        package_service,
    ) -> None:

        self.package_service = package_service

    def execute(
        self,
        context: AcquisitionRunContext,
        output_directory: Path,
        archive_root: Path,
    ) -> AcquisitionRunResult:
        """
        Create investor package from review.
        """

        package_location = self.package_service.create_package(
           context.review,
            output_directory,
            archive_root,
        )

        primary_card = context.review.cards[0]

        return AcquisitionRunResult(
            recommendation=primary_card.recommendation,
            confidence=primary_card.confidence,
            package_location=package_location,
        )
