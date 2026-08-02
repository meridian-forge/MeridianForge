from pathlib import Path

from meridianforge.services.monday_execution_orchestrator import (
    MondayExecutionOrchestrator,
)


def test_execution_orchestrator_runs_without_gmail_sync(
    tmp_path: Path,
) -> None:
    inbox = tmp_path / "inbox"
    inbox.mkdir()

    (inbox / "deal.pdf").write_text(
        "Location: Rosharon, TX\nPrice: $339,000\nRent: $3,135\n"
    )

    orchestrator = MondayExecutionOrchestrator(
        inbox=inbox,
    )

    result = orchestrator.execute(
        synchronize_gmail=False,
    )

    assert result.gmail_synchronized is False
    assert result.operations.artifacts_processed == 1
    assert len(result.operations.routed_extractors) == 1
