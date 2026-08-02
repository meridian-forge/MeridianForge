"""
Monday execution orchestrator.

SP-430.2

Synchronizes Gmail (when enabled) and then executes the adaptive Monday
operations workflow against the local inbox directory.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from meridianforge.connectors.gmail_connector import GmailConnector
from meridianforge.services.monday_operations_orchestrator import (
    MondayOperationsOrchestrator,
    MondayOperationsResult,
)


@dataclass(frozen=True, slots=True)
class MondayExecutionResult:
    """
    Result of a Monday execution run.
    """

    gmail_synchronized: bool
    operations: MondayOperationsResult


class MondayExecutionOrchestrator:
    """
    Execute the full Monday synchronization and operations workflow.
    """

    def __init__(
        self,
        inbox: Path,
        operations: MondayOperationsOrchestrator | None = None,
        gmail: GmailConnector | None = None,
    ) -> None:
        self._inbox = inbox
        self._operations = operations or MondayOperationsOrchestrator()
        self._gmail = gmail or GmailConnector()

    def execute(
        self,
        synchronize_gmail: bool = True,
    ) -> MondayExecutionResult:
        """
        Synchronize Gmail (optional) and execute Monday operations.
        """

        gmail_synchronized = False

        if synchronize_gmail:
            self._gmail.sync(self._inbox)
            gmail_synchronized = True

        operations = self._operations.execute(
            self._inbox,
        )

        return MondayExecutionResult(
            gmail_synchronized=gmail_synchronized,
            operations=operations,
        )
