from meridianforge.cli.monday_command import (
    run_monday,
)


def test_monday_command_creates_dashboard(
    tmp_path,
    monkeypatch,
) -> None:

    monkeypatch.chdir(tmp_path)

    output = run_monday()

    assert output.exists()

    content = output.read_text()

    assert "Meridian Forge Monday Dashboard" in content
