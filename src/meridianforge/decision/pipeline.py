"""
Acquisition decision pipeline.

Transforms acquisition inputs into investor decisions.
"""


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

    def evaluate(
        self,
        opportunity: AcquisitionInput,
    ) -> WeeklyInvestorReview:
        """
        Evaluate acquisition opportunity.
        """

        raise NotImplementedError
