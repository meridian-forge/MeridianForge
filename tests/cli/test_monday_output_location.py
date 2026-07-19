from pathlib import Path

from meridianforge.cli.monday_command import (
    run_monday,
)


def test_monday_dashboard_written_to_runtime_output() -> None:
    output = run_monday()

    assert output == Path("runtime/outputs/MeridianForge_Monday_Dashboard.md")

    assert output.exists()
