import subprocess
import sys
from pathlib import Path


def test_monday_cli_file_input(tmp_path: Path) -> None:
    csv_file = tmp_path / "properties.csv"

    csv_file.write_text(
        "name,status,score,rent,price\n"
        "Property A,BUY,95,2200,250000\n"
        "Property B,WATCH,70,1800,200000\n",
        encoding="utf-8",
    )

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "meridianforge",
            "monday",
            "--file",
            str(csv_file),
        ],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0

    assert "Meridian Forge Monday Workflow" in result.stdout

    assert "Status: COMPLETE" in result.stdout

    assert Path("runtime/outputs/MeridianForge_Monday_Dashboard.md").exists()
