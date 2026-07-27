from pathlib import Path

from meridianforge.intake.file_scanner import scan_directory


def test_scan_directory(tmp_path: Path) -> None:
    (tmp_path / "deal.xlsx").touch()
    (tmp_path / "notes.txt").touch()
    (tmp_path / "offering.pdf").touch()
    (tmp_path / "summary.docx").touch()
    (tmp_path / "readme.rtf").touch()
    (tmp_path / "image.png").touch()

    results = scan_directory(str(tmp_path))

    names = {path.name for path in results}

    assert len(results) == 5

    assert names == {
        "deal.xlsx",
        "notes.txt",
        "offering.pdf",
        "summary.docx",
        "readme.rtf",
    }
