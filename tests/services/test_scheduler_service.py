from __future__ import annotations

import json
from datetime import datetime
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


def test_before_scheduled_window_does_not_execute(tmp_path, monkeypatch):
    service = make_service(tmp_path)
    write_config(service._runtime_root)

    FrozenDateTime.current = datetime(2026, 8, 17, 6, 59)
    monkeypatch.setattr(
        scheduler_module,
        "datetime",
        FrozenDateTime,
    )

    result = service.run_if_due()

    assert result.executed is False
    assert result.reason == "before scheduled window"


def test_after_catch_up_window_does_not_execute(tmp_path, monkeypatch):
    service = make_service(tmp_path)
    write_config(service._runtime_root)

    FrozenDateTime.current = datetime(2026, 8, 17, 17, 0)
    monkeypatch.setattr(
        scheduler_module,
        "datetime",
        FrozenDateTime,
    )

    result = service.run_if_due()

    assert result.executed is False
    assert result.reason == "after catch-up window"


def test_not_scheduled_today_does_not_execute(tmp_path, monkeypatch):
    service = make_service(tmp_path)
    write_config(
        service._runtime_root,
        mode="monday",
    )

    FrozenDateTime.current = datetime(2026, 8, 18, 9, 0)
    monkeypatch.setattr(
        scheduler_module,
        "datetime",
        FrozenDateTime,
    )

    result = service.run_if_due()

    assert result.executed is False
    assert result.reason == "not scheduled today"


def test_daily_scheduler_executes(tmp_path, monkeypatch):
    service = make_service(tmp_path)
    write_config(service._runtime_root)

    execution = Mock()
    execution.monday_report = "# Report\n"
    execution.operations.artifacts_processed = 1
    execution.operations.normalized_opportunities = []
    execution.operations.audit_report = "# Audit\n"

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
        "datetime",
        FrozenDateTime,
    )
    monkeypatch.setattr(
        scheduler_module,
        "MondayExecutionOrchestrator",
        lambda inbox: orchestrator,
    )
    monkeypatch.setattr(
        scheduler_module,
        "DashboardPublisherService",
        lambda: publisher,
    )
    monkeypatch.setattr(
        scheduler_module,
        "MorningBriefingService",
        lambda recipient: briefing,
    )

    result = service.run_if_due()

    assert result.executed is True
    assert result.success is True
    assert result.reason == "executed"
    orchestrator.execute.assert_called_once_with(
        synchronize_gmail=True,
    )
    publisher.publish.assert_called_once_with(
        execution,
    )
    briefing.send.assert_called_once()


def test_successful_run_same_day_can_execute_again(
    tmp_path,
    monkeypatch,
):
    service = make_service(tmp_path)
    write_config(service._runtime_root)

    service._state_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    service._state_path.write_text(
        json.dumps(
            {
                "last_successful_run": "2026-08-17",
                "last_finished_at": "2026-08-17T08:00:00",
            }
        ),
        encoding="utf-8",
    )

    FrozenDateTime.current = datetime(
        2026,
        8,
        17,
        9,
        0,
    )

    execution = Mock()
    execution.monday_report = "# Report\n"
    execution.operations.artifacts_processed = 0
    execution.operations.normalized_opportunities = []
    execution.operations.audit_report = "# Audit\n"

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
        "datetime",
        FrozenDateTime,
    )
    monkeypatch.setattr(
        scheduler_module,
        "MondayExecutionOrchestrator",
        lambda inbox: orchestrator,
    )
    monkeypatch.setattr(
        scheduler_module,
        "DashboardPublisherService",
        lambda: publisher,
    )
    monkeypatch.setattr(
        scheduler_module,
        "MorningBriefingService",
        lambda recipient: briefing,
    )

    result = service.run_if_due()

    assert result.executed is True
    assert result.success is True
    assert result.reason == "executed"
    orchestrator.execute.assert_called_once_with(
        synchronize_gmail=True,
    )


def test_invalid_config_uses_safe_defaults(tmp_path, monkeypatch):
    service = make_service(tmp_path)

    config_path = service._runtime_root / "config" / "scheduler.json"
    config_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )
    config_path.write_text(
        "{ invalid json",
        encoding="utf-8",
    )

    FrozenDateTime.current = datetime(
        2026,
        8,
        17,
        6,
        59,
    )

    monkeypatch.setattr(
        scheduler_module,
        "datetime",
        FrozenDateTime,
    )

    result = service.run_if_due()

    assert result.executed is False
    assert result.reason == "before scheduled window"


def test_custom_weekday_configuration(tmp_path):
    service = make_service(tmp_path)

    assert service._is_due_today(
        datetime(2026, 8, 17).date(),
        {
            "mode": "custom",
            "weekdays": [1],
        },
    )

    assert not service._is_due_today(
        datetime(2026, 8, 18).date(),
        {
            "mode": "custom",
            "weekdays": [1],
        },
    )


def test_load_state_missing_file_returns_empty(tmp_path):
    service = make_service(tmp_path)

    assert service._load_state() == {}


def test_save_and_load_state(tmp_path):
    service = make_service(tmp_path)

    service._save_state(
        {
            "last_successful_run": "2026-08-17",
            "last_finished_at": "2026-08-17T10:00:00",
        }
    )

    assert service._load_state() == {
        "last_successful_run": "2026-08-17",
        "last_finished_at": "2026-08-17T10:00:00",
    }
