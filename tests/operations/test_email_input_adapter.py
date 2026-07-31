from pathlib import Path

from meridianforge.operations.email_input_adapter import (
    EmailInputAdapter,
)


def test_email_adapter_discovers_files(
    tmp_path: Path,
) -> None:
    (tmp_path / "portfolio.xlsx").write_text("x")
    (tmp_path / "offering.pdf").write_text("p")
    (tmp_path / "subdir").mkdir()

    adapter = EmailInputAdapter(
        tmp_path,
    )

    files = adapter.discover()

    assert len(files) == 2
    assert files[0].name == "offering.pdf"
    assert files[1].name == "portfolio.xlsx"
