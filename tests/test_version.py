from pathlib import Path


def test_version_exists() -> None:

    version_file = Path("VERSION")

    assert version_file.exists()
    assert version_file.read_text().strip() == "1.0.0-MVP"
