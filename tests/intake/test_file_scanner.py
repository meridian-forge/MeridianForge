from pathlib import Path

from meridianforge.intake.file_scanner import scan_directory


def test_scan_directory(tmp_path: Path) -> None:
    (tmp_path / "deal.xlsx").touch()
    (tmp_path / "notes.txt").touch()

    results = scan_directory(str(tmp_path))

    assert len(results) == 1
