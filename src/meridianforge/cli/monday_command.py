"""
Monday CLI command.

SP-430.2

Routes the Monday command through the OperationsService.
"""

from pathlib import Path

from meridianforge.models.operations import OperationsRunResult
from meridianforge.services.operations_service import OperationsService


def run_monday() -> OperationsRunResult:
    """
    Execute the MeridianForge Monday operational workflow.
    """

    runtime_root = Path("runtime")

    deals_directory = runtime_root / "incoming" / "deals"

    service = OperationsService(
        deals_directory=deals_directory,
    )

    result = service.execute()

    print()
    print("====================================")
    print("MeridianForge Monday Operations")
    print("====================================")
    print(f"Deals discovered : {result.total_files}")
    print(f"Deals processed  : {len(result.files_processed)}")
    print(f"Failures         : {len(result.failed_files)}")
    print(f"Success          : {result.success}")
    print("====================================")
    print()

    return result
