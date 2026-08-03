from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class GmailExecutionLedgerResult:
    processed: bool
    archived: bool


class GmailExecutionLedgerService:
    """
    Record processed Gmail messages and prevent duplicate execution.

    SP-480.4
    """

    def __init__(
        self,
        ledger_path: Path,
    ) -> None:
        self._ledger_path = ledger_path

        self._ledger_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        if not self._ledger_path.exists():
            self._ledger_path.write_text(
                "",
                encoding="utf-8",
            )

    def already_processed(
        self,
        message_id: str,
    ) -> bool:
        entries = set(
            self._ledger_path.read_text(
                encoding="utf-8",
            ).splitlines()
        )

        return message_id in entries

    def mark_processed(
        self,
        message_id: str,
    ) -> GmailExecutionLedgerResult:
        if self.already_processed(
            message_id,
        ):
            return GmailExecutionLedgerResult(
                processed=False,
                archived=False,
            )

        with self._ledger_path.open(
            "a",
            encoding="utf-8",
        ) as handle:
            handle.write(f"{message_id}\n")

        return GmailExecutionLedgerResult(
            processed=True,
            archived=True,
        )
