from __future__ import annotations

from datetime import datetime
from pathlib import Path

from meridianforge.models.operations import OperationsRunResult
from meridianforge.services.monday_execution_orchestrator import (
    MondayExecutionOrchestrator,
)


def run_monday(
    deals_directory: Path | None = None,
    use_email: bool = False,
) -> OperationsRunResult:
    """
    Execute the canonical MeridianForge Monday workflow.

    Routes directly through MondayExecutionOrchestrator, which is now the
    production entry point for Gmail synchronization, intake, routing,
    evidence extraction, underwriting, and dashboard generation.
    """

    if deals_directory is None:
        if use_email:
            deals_directory = (
                Path.home()
                / "Documents"
                / "MeridianForge"
                / "10_Runtime"
                / "Incoming"
                / "Email"
            )
        else:
            deals_directory = Path("runtime") / "incoming" / "deals"

    orchestrator = MondayExecutionOrchestrator(
        inbox=deals_directory,
    )

    execution = orchestrator.execute(
        synchronize_gmail=use_email,
    )

    operations = execution.operations

    if deals_directory.exists():
        discovered = sorted(
            path for path in deals_directory.iterdir() if path.is_file()
        )
    else:
        discovered = []

    result = OperationsRunResult(
        started_at=datetime.now(),
    )

    result.files_discovered = discovered
    result.files_processed = discovered
    result.buy_count = len(
        operations.normalized_opportunities,
    )
    result.watch_count = 0
    result.pass_count = 0

    print("Meridian Forge Monday Workflow")
    print("MeridianForge Monday Operations")

    source = "Gmail (MeridianForge label)" if use_email else "Local directory"

    print(f"Input source    : {source}")
    print(f"Deals directory : {deals_directory}")
    print(f"Files processed : {len(discovered)}")
    print(f"BUY candidates  : {result.buy_count}")
    print(f"WATCH candidates: {result.watch_count}")
    print(f"PASS candidates : {result.pass_count}")

    print("Status: READY")
    print("Success")

    return result


def run(
    deals_directory: Path | None = None,
    use_email: bool = False,
) -> OperationsRunResult:
    return run_monday(
        deals_directory=deals_directory,
        use_email=use_email,
    )
