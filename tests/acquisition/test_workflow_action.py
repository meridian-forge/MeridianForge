from meridianforge.acquisition.workflow_action import (
    WorkflowAction,
)


def test_workflow_action_creation():

    action = WorkflowAction(
        action="PREPARE_OFFER",
        priority="HIGH",
        reason="Strong acquisition candidate",
    )

    assert action.action == "PREPARE_OFFER"
    assert action.priority == "HIGH"
