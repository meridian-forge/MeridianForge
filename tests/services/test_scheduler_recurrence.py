from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from types import SimpleNamespace

import meridianforge.services.scheduler_service as scheduler_module
from meridianforge.services.scheduler_service import SchedulerService


class FrozenDateTime(datetime):
    current = datetime(2026, 8, 17, 10, 0)

    @classmethod
    def now(cls, tz=None):
        if tz is None:
            return cls.current
        return cls.current.replace(tzinfo=tz)


def test_scheduler_does_not_block_second_run_same_day(
    tmp_path: Path,
    monkeypatch,
) -> None:
    runtime_root = tmp_path / "runtime"
    inbox = runtime_root / "Incoming" / "Email"
    state_path = runtime_root / "State" / "scheduler_state.json"

    config_path = runtime_root / "config" / "scheduler.json"
    config_path.parent.mkdir(parents=True, exist_ok=True)
    config_path.write_text(
        json.dumps(
            {
                "mode": "daily",
                "timezone": "America/New_York",
                "hour": 7,
                "minute": 0,
                "catch_up_until_hour": 17,
                "weekdays": [1, 2, 3, 4, 5, 6, 7],
                "use_email": True,
            }
        ),
        encoding="utf-8",
    )

    state_path.parent.mkdir(parents=True, exist_ok=True)
    state_path.write_text(
        json.dumps(
            {
                "last_successful_run": "2026-08-17",
                "last_finished_at": "2026-08-17T07:00:00",
            }
        ),
        encoding="utf-8",
    )

    service = SchedulerService(
        runtime_root=runtime_root,
        inbox=inbox,
        state_path=state_path,
    )

    execution = SimpleNamespace(
        gmail_synchronized=True,
        monday_report="# Monday report\n",
        operations=SimpleNamespace(
            artifacts_processed=1,
            normalized_opportunities=[],
            audit_report="# Audit\n",
        ),
    )

    class FakeOrchestrator:
        calls = []

        def __init__(self, inbox):
            self.inbox = inbox

        def execute(self, synchronize_gmail):
            self.calls.append(synchronize_gmail)
            return execution

    published = SimpleNamespace(
        public_url="https://meridian-forge.github.io/meridian-dashboard/",
    )

    class FakePublisher:
        def publish(self, value):
            assert value is execution
            return published

    class FakeBriefing:
        def __init__(self, recipient):
            assert recipient == "teknostrata@gmail.com"

        def send(self, execution, dashboard_url):
            assert execution is not None
            assert dashboard_url == published.public_url

    monkeypatch.setattr(
        scheduler_module,
        "datetime",
        FrozenDateTime,
    )
    monkeypatch.setattr(
        scheduler_module,
        "MondayExecutionOrchestrator",
        FakeOrchestrator,
    )
    monkeypatch.setattr(
        scheduler_module,
        "DashboardPublisherService",
        FakePublisher,
    )
    monkeypatch.setattr(
        scheduler_module,
        "MorningBriefingService",
        FakeBriefing,
    )

    result = service.run_if_due()

    assert result.executed is True
    assert result.success is True
    assert result.reason == "executed"
    assert FakeOrchestrator.calls == [True]
    assert state_path.exists()
