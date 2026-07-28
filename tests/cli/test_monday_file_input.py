import subprocess
import sys
from pathlib import Path


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
    assert "MeridianForge Monday Operations" in result.stdout
    assert "Success" in result.stdout
