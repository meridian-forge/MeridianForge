from __future__ import annotations

from meridianforge.services.gmail_execution_ledger_service import (
    GmailExecutionLedgerService,
)


def test_prevent_duplicate_execution(tmp_path) -> None:
    ledger = GmailExecutionLedgerService(tmp_path / "gmail_execution_ledger.txt")

    first = ledger.mark_processed("gmail-123")

    second = ledger.mark_processed("gmail-123")

    assert first.processed is True
    assert first.archived is True

    assert second.processed is False
    assert second.archived is False

    assert ledger.already_processed("gmail-123") is True
