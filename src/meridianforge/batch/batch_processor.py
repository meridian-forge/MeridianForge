"""
Batch acquisition processor.

Runs multiple acquisition opportunities
through the decision workflow.
"""

from meridianforge.batch.batch_request import (
    BatchRequest,
)
from meridianforge.batch.batch_result import (
    BatchResult,
)
from meridianforge.workflows.acquisition_decision_workflow import (
    AcquisitionDecisionWorkflow,
)


class BatchProcessor:
    """
    Executes acquisition decisions in batch.
    """

    def __init__(
        self,
        decision_workflow: AcquisitionDecisionWorkflow | None = None,
    ) -> None:

        self.decision_workflow = (
            decision_workflow
            or AcquisitionDecisionWorkflow()
        )

    def process(
        self,
        request: BatchRequest,
    ) -> BatchResult:
        """
        Process all acquisition opportunities.
        """

        reviews = []

        for opportunity in request.opportunities:

            review = self.decision_workflow.execute(
                opportunity,
            )

            reviews.append(review)

        return BatchResult(
            reviews=reviews,
        )
