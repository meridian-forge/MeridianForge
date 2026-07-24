"""
Acquisition workflow action model.

MF-340.3

Represents operational next steps
generated from acquisition intelligence.
"""

from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True, init=False)
class WorkflowAction:
    """
    Operational workflow instruction.
    """

    action_type: str

    status: str

    priority: str

    reason: str

    notes: list[str]

    created_at: datetime

    def __init__(
        self,
        action_type: str | None = None,
        status: str = "OPEN",
        priority: str = "MEDIUM",
        reason: str = "",
        notes: list[str] | None = None,
        created_at: datetime | None = None,
        action: str | None = None,
    ) -> None:

        self.action_type = (
            action_type
            if action_type is not None
            else action if action is not None else ""
        )

        self.status = status
        self.priority = priority
        self.reason = reason

        self.notes = notes if notes is not None else []

        self.created_at = created_at if created_at is not None else datetime.now()

    @property
    def action(self) -> str:
        """
        Backward-compatible alias.
        """

        return self.action_type
