from pathlib import Path

from meridianforge.services.monday_operations_orchestrator import (
    MondayOperationsOrchestrator,
)


def test_monday_operations_orchestrator_processes_inbox(
    tmp_path: Path,
) -> None:
    inbox = tmp_path / "inbox"
    inbox.mkdir()

    (inbox / "deal.pdf").write_text(
        "Location: Rosharon, TX\nPrice: $339,000\nRent: $3,135\n"
    )

    orchestrator = MondayOperationsOrchestrator()

    result = orchestrator.execute(
        inbox,
    )

    assert result.artifacts_processed == 1
    assert len(result.routed_extractors) == 1
    assert "Extraction Audit Dashboard" in result.audit_report
