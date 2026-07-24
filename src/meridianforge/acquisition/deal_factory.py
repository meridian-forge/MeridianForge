"""
Deal factory.

MF-338.3

Creates workflow deals from acquisition results.
"""

from meridianforge.acquisition.deal_pipeline import (
    DealPipeline,
)
from meridianforge.acquisition.pipeline_stage import (
    PipelineStage,
)
from meridianforge.acquisition.result import (
    AcquisitionResult,
)


class DealFactory:
    """
    Converts acquisition intelligence
    into managed deals.
    """

    @staticmethod
    def create(
        result: AcquisitionResult,
    ) -> DealPipeline:
        """
        Create deal pipeline record.
        """

        opportunity = result.opportunity

        address = (
            f"{opportunity.address}, "
            f"{opportunity.city}, "
            f"{opportunity.state} "
            f"{opportunity.zip_code}"
        )

        stage = (
            PipelineStage.REVIEW
            if result.recommendation == "BUY"
            else PipelineStage.ANALYZING
        )

        return DealPipeline(
            property_address=address,
            stage=stage,
            score=result.score,
            recommendation=result.recommendation,
        )
