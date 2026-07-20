"""
Acquisition decision workflow.

Coordinates acquisition input through
decision evaluation and investor review.
"""

from meridianforge.decision.pipeline import (
    DecisionPipeline,
)
from meridianforge.product.weekly_review import (
    WeeklyInvestorReview,
)
from meridianforge.workflows.acquisition_input import (
    AcquisitionInput,
)


class AcquisitionDecisionWorkflow:
    """
    End-to-end acquisition decision coordinator.
    """

    def __init__(
        self,
        decision_pipeline: DecisionPipeline | None = None,
    ) -> None:

        self.decision_pipeline = (
            decision_pipeline
            or DecisionPipeline()
        )

    def execute(
        self,
        opportunity: AcquisitionInput,
    ) -> WeeklyInvestorReview:
        """
        Evaluate acquisition opportunity.
        """

        return self.decision_pipeline.evaluate(
            opportunity,
        )
