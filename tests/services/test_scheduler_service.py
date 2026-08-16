from __future__ import annotations

import json
from datetime import date, datetime
from pathlib import Path
from unittest.mock import Mock

import meridianforge.services.scheduler_service as scheduler_module
from meridianforge.services.scheduler_service import SchedulerService


class FrozenDateTime(datetime):
    current: datetime = datetime(2026, 8, 17, 7, 0)

    @classmethod
    def now(cls, tz=None):
        if tz is None:
            return cls.current
        return cls.current.replace(tzinfo=tz)


def write_config(runtime_root: Path, **overrides: object) -> None:
    config = {
        "mode": "daily",
        "timezone": "America/New_York",
        "hour": 7,
        "minute": 0,
        "catch_up_until_hour": 17,
        "weekdays": [1, 2, 3, 4, 5, 6, 7],
        "use_email": True,
    }
    config.update(overrides)

    config_path = runtime_root / "config" / "scheduler.json"
    config_path.parent.mkdir(parents=True, exist_ok=True)
    config_path.write_text(
        json.dumps(config),
        encoding="utf-8",
    )


def make_service(tmp_path: Path) -> SchedulerService:
    runtime_root = tmp_path / "runtime"
    return SchedulerService(
        runtime_root=runtime_root,
        inbox=runtime_root / "Incoming" / "Email",
        state_path=runtime_root / "State" / "scheduler_state.json",
    )


def test_daily_schedule_is_due_every_day():
    service = make_service(Path("/tmp") / "meridianforge-scheduler-test-daily")
    config = {"mode": "daily"}

    assert service._is_due_today(date(2026, 8, 16), config) is True
    assert service._is_due_today(date(2026, 8, 17), config) is True


def test_monday_schedule_only_runs_on_monday():
    service = make_service(Path("/tmp") / "meridianforge-scheduler-test-monday")
    config = {"mode": "monday"}

    assert service._is_due_today(date(2026, 8, 17), config) is True
    assert service._is_due_today(date(2026, 8, 18), config) is False


def test_weekdays_schedule_excludes_weekends():
    service = make_service(Path("/tmp") / "meridianforge-scheduler-test-weekdays")
    config = {"mode": "weekdays"}

    assert service._is_due_today(date(2026, 8, 17), config) is True
    assert service._is_due_today(date(2026, 8, 22), config) is False
    assert service._is_due_today(date(2026, 8, 23), config) is False


def test_custom_schedule_uses_configured_weekday_numbers():
    service = make_service(Path("/tmp") / "meridianforge-scheduler-test-custom")
    config = {"mode": "custom", "weekdays": [1, 3, 5]}

    assert service._is_due_today(date(2026, 8, 17), config) is True
    assert service._is_due_today(date(2026, 8, 18), config) is False
    assert service._is_due_today(date(2026, 8, 19), config) is True


def test_before_scheduled_time_does_not_execute(tmp_path, monkeypatch):
    service = make_service(tmp_path)
    write_config(service._runtime_root)

    FrozenDateTime.current = datetime(2026, 8, 17, 6, 59)
    monkeypatch.setattr(scheduler_module, "datetime", FrozenDateTime)

    result = service.run_if_due()

    assert result.executed is False
    assert result.reason == "before scheduled window"


def test_after_catch_up_window_does_not_execute(tmp_path, monkeypatch):
    service = make_service(tmp_path)
    write_config(service._runtime_root)

    FrozenDateTime.current = datetime(2026, 8, 17, 17, 0)
    monkeypatch.setattr(scheduler_module, "datetime", FrozenDateTime)

    result = service.run_if_due()

    assert result.executed is False
    assert result.reason == "after catch-up window"


def test_already_successful_today_does_not_execute(tmp_path, monkeypatch):
    service = make_service(tmp_path)
    write_config(service._runtime_root)

    service._state_path.parent.mkdir(parents=True, exist_ok=True)
    service._state_path.write_text(
        json.dumps(
            {
                "last_successful_run": "2026-08-17",
                "last_finished_at": "2026-08-17T08:00:00",
            }
        ),
        encoding="utf-8",
    )

    FrozenDateTime.current = datetime(2026, 8, 17, 9, 0)
    monkeypatch.setattr(scheduler_module, "datetime", FrozenDateTime)

    result = service.run_if_due()

    assert result.executed is False
    assert result.reason == "already executed today"


def test_due_run_executes_and_records_success(tmp_path, monkeypatch):
    service = make_service(tmp_path)
    write_config(service._runtime_root)

    execution = Mock()
    execution.monday_report = "# Monday report"

    orchestrator = Mock()
    orchestrator.execute.return_value = execution

    publisher_result = Mock()
    publisher_result.public_url = (
        "https://meridian-forge.github.io/meridian-dashboard/"
    )

    publisher = Mock()
    publisher.publish.return_value = publisher_result

    briefing = Mock()

    monkeypatch.setattr(
        scheduler_module,
        "MondayExecutionOrchestrator",
        Mock(return_value=orchestrator),
    )
    monkeypatch.setattr(
        scheduler_module,
        "DashboardPublisherService",
        Mock(return_value=publisher),
    )
    monkeypatch.setattr(
        scheduler_module,
        "MorningBriefingService",
        Mock(return_value=briefing),
    )

    FrozenDateTime.current = datetime(2026, 8, 17, 9, 0)
    monkeypatch.setattr(scheduler_module, "datetime", FrozenDateTime)

    result = service.run_if_due()

    assert result.executed is True
    assert result.reason == "executed"
    assert result.success is True
    assert result.report_path == (
        service._runtime_root / "reports" / "monday_operations_report.md"
    )
    assert result.dashboard_url == publisher_result.public_url

    orchestrator.execute.assert_called_once_with(
        synchronize_gmail=True,
    )
    publisher.publish.assert_called_once_with(execution)
    briefing.send.assert_called_once_with(
        execution=execution,
        dashboard_url=publisher_result.public_url,
    )

    state = json.loads(
        service._state_path.read_text(encoding="utf-8")
    )
    assert state["last_successful_run"] == "2026-08-17"
    assert state["last_finished_at"] == "2026-08-17T09:00:00"

    assert result.report_path.read_text(encoding="utf-8") == "# Monday report"
