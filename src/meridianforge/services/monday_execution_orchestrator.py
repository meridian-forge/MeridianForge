"""
Monday execution orchestrator.

SP-430.3

Executes the end-to-end Monday production workflow:
Gmail synchronization -> intake -> adaptive routing -> audit reporting ->
consolidated Monday operations report.
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
    monday_report: str


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

        report = self._build_report(
            gmail_synchronized=gmail_synchronized,
            operations=operations,
        )

        return MondayExecutionResult(
            gmail_synchronized=gmail_synchronized,
            operations=operations,
            monday_report=report,
        )

    def _build_report(
        self,
        *,
        gmail_synchronized: bool,
        operations: MondayOperationsResult,
    ) -> str:
        """
        Build the consolidated Monday operations report.
        """

        extractors = (
            "\n".join(f"- {name}" for name in operations.routed_extractors)
            if operations.routed_extractors
            else "- None"
        )

        return (
            "# MeridianForge Monday Operations Report\n\n"
            f"Gmail synchronized: {'Yes' if gmail_synchronized else 'No'}\n"
            f"Artifacts processed: {operations.artifacts_processed}\n\n"
            "## Routed extractors\n"
            f"{extractors}\n\n"
            "## Extraction audit\n\n"
            f"{operations.audit_report}\n"
        )
