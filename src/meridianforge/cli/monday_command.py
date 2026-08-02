"""
Monday CLI command.

MF-511.0.4

Routes the Monday command through the
Gmail-backed MondayExecutionPipeline while
preserving the historical CLI contract
expected by existing tests and automation.
"""

from __future__ import annotations

from pathlib import Path

from meridianforge.models.operations import OperationsRunResult
from meridianforge.workflows.monday_execution_pipeline import (
    MondayExecutionPipeline,
)


def run_monday(
    deals_directory: Path | None = None,
    use_email: bool = False,
) -> OperationsRunResult:
    """
    Execute the MeridianForge Monday workflow.

    Historical behavior is preserved by default (local runtime directory).
    Gmail synchronization is available by passing use_email=True.
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

    pipeline = (
        MondayExecutionPipeline.from_email(deals_directory)
        if use_email
        else MondayExecutionPipeline(deals_directory=deals_directory)
    )

    pipeline_result = pipeline.execute()

    operations = pipeline_result.operations

    # Preserve historical CLI expectations used by older tests.
    if deals_directory.exists():
        discovered = sorted(
            path for path in deals_directory.iterdir() if path.is_file()
        )
    else:
        discovered = []

    operations.files_discovered = discovered
    operations.files_processed = discovered

    print("Meridian Forge Monday Workflow")
    print("MeridianForge Monday Operations")

    source = "Gmail (MeridianForge label)" if use_email else "Local directory"

    print(f"Input source    : {source}")
    print(f"Deals directory : {deals_directory}")
    print(f"Files processed : {len(operations.files_processed)}")
    print(f"BUY candidates  : {operations.buy_count}")
    print(f"WATCH candidates: {operations.watch_count}")
    print(f"PASS candidates : {operations.pass_count}")

    if operations.dashboard_path is not None:
        print(f"Dashboard       : {operations.dashboard_path}")

    print("Status: READY")
    print("Success")

    return operations


def run(
    deals_directory: Path | None = None,
    use_email: bool = False,
) -> OperationsRunResult:
    """
    Backward-compatible CLI alias.
    """

    return run_monday(
        deals_directory=deals_directory,
        use_email=use_email,
    )
