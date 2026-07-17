"""
Acquisition pipeline.

Coordinates acquisition workflow and
returns standardized acquisition results.
"""

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
    ) -> AcquisitionResult:
        """
        Process analyzed assets into an acquisition result.
        """

        return AcquisitionResult(
            confidence=confidence,
            assets_analyzed=len(assets),
            warnings=warnings or [],
        )
