"""
Acquisition pipeline.

Coordinates acquisition workflow and
connects underwriting assessment.
"""

from meridianforge.models.results.acquisition_assessment import (
    AcquisitionAssessment,
)
from meridianforge.models.results.acquisition_result import (
    AcquisitionResult,
)


class AcquisitionPipeline:
    """
    Main acquisition workflow coordinator.
    """

    def process(
        self,
        assets: list[dict[str, object]],
        confidence: float = 0.0,
        warnings: list[str] | None = None,
        assessment: AcquisitionAssessment | None = None,
    ) -> AcquisitionResult:
        """
        Process acquisition workflow.
        """

        metadata: dict[str, object] = {}

        if assessment:
            metadata["assessment"] = assessment

        return AcquisitionResult(
            confidence=confidence,
            assets_analyzed=len(assets),
            warnings=warnings or [],
            metadata=metadata,
        )
