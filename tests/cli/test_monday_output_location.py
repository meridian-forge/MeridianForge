from pathlib import Path

from meridianforge.cli.monday_command import run_monday


def test_monday_returns_operations_result(
    tmp_path,
    monkeypatch,
) -> None:
    monkeypatch.chdir(tmp_path)

    Path("runtime/incoming/deals").mkdir(parents=True)

    result = run_monday()

    assert result.dashboard_path is None
    assert result.success
