from pathlib import Path

from meridianforge.cli.monday_command import run_monday


def test_monday_command_discovers_runtime_deals(
    tmp_path,
    monkeypatch,
) -> None:
    monkeypatch.chdir(tmp_path)

    deals = Path("runtime/incoming/deals")
    deals.mkdir(parents=True)

    (deals / "property.xlsx").write_text("test")

    result = run_monday()

    assert result.success
    assert result.total_files == 1
    assert len(result.files_discovered) == 1
