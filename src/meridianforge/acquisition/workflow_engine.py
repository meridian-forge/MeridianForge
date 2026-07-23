"""
Workflow automation engine.

MF-340.2

Creates workflow actions from
acquisition intelligence.
"""

from meridianforge.acquisition.result import (
    AcquisitionResult,
)

from meridianforge.acquisition.workflow_action import (
    WorkflowAction,
)


class WorkflowEngine:
    """
    Converts acquisition decisions
    into operational tasks.
    """

    @staticmethod
    def generate(
        result: AcquisitionResult,
    ) -> list[WorkflowAction]:
        """
        Generate workflow actions.
        """

        actions: list[WorkflowAction] = []

        if result.recommendation == "BUY":

            actions.append(
                WorkflowAction(
                    action_type="REVIEW_FOR_OFFER",
                    status="OPEN",
                    priority="HIGH",
                )
            )

            actions.append(
                WorkflowAction(
                    action_type="REQUEST_FINANCING",
                    status="OPEN",
                    priority="MEDIUM",
                )
            )

            actions.append(
                WorkflowAction(
                    action_type="ADD_TO_PIPELINE",
                    status="OPEN",
                    priority="HIGH",
                )
            )

        else:

            actions.append(
                WorkflowAction(
                    action_type="ANALYST_REVIEW",
                    status="OPEN",
                    priority="MEDIUM",
                )
            )

        return actions
