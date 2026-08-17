import subprocess
import sys


def test_monday_cli_runs() -> None:
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "meridianforge",
            "monday",
        ],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    assert "Meridian Forge Monday Workflow" in result.stdout
    assert "Status: COMPLETE" in result.stdout
