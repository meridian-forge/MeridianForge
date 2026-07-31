from pathlib import Path

from meridianforge.operations.directory_input_adapter import (
    DirectoryInputAdapter,
)


def test_directory_adapter_discovers_files(
    tmp_path: Path,
) -> None:
    (tmp_path / "a.xlsx").write_text("a")
    (tmp_path / "b.pdf").write_text("b")
    (tmp_path / "folder").mkdir()

    adapter = DirectoryInputAdapter(
        tmp_path,
    )

    files = adapter.discover()

    assert len(files) == 2
    assert files[0].name == "a.xlsx"
    assert files[1].name == "b.pdf"
