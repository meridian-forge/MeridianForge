from pathlib import Path


def test_version_exists() -> None:

    version_file = Path("VERSION")

    assert version_file.exists()

    version = version_file.read_text(
        encoding="utf-8",
    ).strip()

    assert version
    assert version.count(".") == 2
