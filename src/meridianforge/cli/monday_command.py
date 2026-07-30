"""
Monday CLI command.

MF-504.2

Routes the Monday command through the
OperationsService while preserving
the original CLI contract expected
by the existing test suite.
"""

from __future__ import annotations

from pathlib import Path

from meridianforge.models.operations import OperationsRunResult
from meridianforge.services.operations_service import OperationsService


def run_monday(
    deals_directory: Path | None = None,
) -> OperationsRunResult:
    """
    Execute the MeridianForge Monday automation workflow.

    Backward-compatible behavior:
    - If no directory is provided, use runtime/incoming/deals.
    - Existing CLI entrypoints and tests continue to work.
    """

    if deals_directory is None:
        deals_directory = Path("runtime") / "incoming" / "deals"

    service = OperationsService(deals_directory)
    result = service.execute()

    print("Meridian Forge Monday Workflow")
    print("MeridianForge Monday Operations")
    print(f"Deals directory : {deals_directory}")
    print(f"Files processed : {len(result.files_processed)}")
    print(f"BUY candidates  : {result.buy_count}")
    print(f"WATCH candidates: {result.watch_count}")
    print(f"PASS candidates : {result.pass_count}")

    if result.dashboard_path is not None:
        print(f"Dashboard       : {result.dashboard_path}")

    print("Status: READY")
    print("Success")

    return result


def run(
    deals_directory: Path | None = None,
) -> OperationsRunResult:
    """
    Backward-compatible alias for the CLI entry point.
    """

    return run_monday(
        deals_directory,
    )
