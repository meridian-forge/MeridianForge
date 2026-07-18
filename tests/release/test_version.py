from pathlib import Path


def test_version_exists():

    version = Path("VERSION")

    assert version.exists()
