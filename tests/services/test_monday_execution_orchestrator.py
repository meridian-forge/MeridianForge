from pathlib import Path

from meridianforge.services.monday_execution_orchestrator import (
    MondayExecutionOrchestrator,
)


def test_monday_execution_orchestrator_runs_empty_directory(
    tmp_path: Path,
):

    orchestrator = MondayExecutionOrchestrator(
        deals_directory=tmp_path,
    )

    result = orchestrator.execute()

    assert result.files_processed == 0

    assert result.buy_count == 0

    assert result.watch_count == 0

    assert result.pass_count == 0
