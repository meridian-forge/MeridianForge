"""
Workflow automation engine.

MF-340.3

Creates operational actions
from acquisition intelligence.
"""

from meridianforge.acquisition.result import (
    AcquisitionResult,
)
from meridianforge.acquisition.workflow_action import (
    WorkflowAction,
)


class WorkflowEngine:
    """
    Generates next acquisition actions.
    """

    @staticmethod
    def generate(
        result: AcquisitionResult,
    ) -> list[WorkflowAction]:

        actions: list[WorkflowAction] = []

        if result.recommendation == "BUY":

            actions.append(
                WorkflowAction(
                    action_type="REVIEW_FOR_OFFER",
                    status="OPEN",
                    priority="HIGH",
                    reason="Strong acquisition candidate",
                )
            )

            actions.append(
                WorkflowAction(
                    action_type="REQUEST_FINANCING",
                    status="OPEN",
                    priority="MEDIUM",
                    reason="Begin financing review",
                )
            )

            actions.append(
                WorkflowAction(
                    action_type="ADD_TO_PIPELINE",
                    status="OPEN",
                    priority="HIGH",
                    reason="Track acquisition progress",
                )
            )

        else:

            actions.append(
                WorkflowAction(
                    action_type="ANALYST_REVIEW",
                    status="OPEN",
                    priority="MEDIUM",
                    reason="Additional review required",
                )
            )

        return actions
