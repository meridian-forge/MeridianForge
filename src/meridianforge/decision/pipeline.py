"""
Acquisition decision pipeline.

Transforms acquisition inputs into investor decisions.
"""

from meridianforge.decision.property_adapter import (
    AcquisitionPropertyAdapter,
)
from meridianforge.engine.underwriting_engine import (
    UnderwritingEngine,
)
from meridianforge.product.weekly_review import (
    WeeklyInvestorReview,
)
from meridianforge.workflows.acquisition_input import (
    AcquisitionInput,
)


class DecisionPipeline:
    """
    Generate investor review decisions.
    """
    
    def __init__(
        self,
        property_adapter=None,
        underwriting_engine=None,
    ):
        self.property_adapter = (
        property_adapter
        or AcquisitionPropertyAdapter()
        )
        self.underwriting_engine = (
        underwriting_engine
        or UnderwritingEngine
        )

    def evaluate(
        self,
        opportunity: AcquisitionInput,
    ) -> WeeklyInvestorReview:
        """
        Evaluate acquisition opportunity.
        """

        raise NotImplementedError
