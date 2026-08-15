from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import date, datetime, time
from pathlib import Path
from zoneinfo import ZoneInfo

from meridianforge.services.dashboard_publisher_service import (
    DashboardPublisherService,
)
from meridianforge.services.monday_execution_orchestrator import (
    MondayExecutionOrchestrator,
)
from meridianforge.services.morning_briefing_service import MorningBriefingService


@dataclass(frozen=True, slots=True)
class SchedulerRunResult:
    executed: bool
    reason: str
    started_at: datetime | None = None
    finished_at: datetime | None = None
    report_path: Path | None = None
    dashboard_url: str | None = None
    success: bool = False


class SchedulerService:
    PRODUCTION_RUNTIME = Path.home() / "Documents" / "MeridianForge" / "10_Runtime"
    DEVELOPMENT_RUNTIME = Path("runtime")

    def __init__(
        self,
        inbox: Path | None = None,
        state_path: Path | None = None,
        runtime_root: Path | None = None,
    ) -> None:
        self._runtime_root = runtime_root or self._detect_runtime_root()
        self._inbox = inbox or (self._runtime_root / "Incoming" / "Email")
        self._state_path = state_path or (
            self._runtime_root / "state" / "scheduler_state.json"
        )
        self._config_path = self._runtime_root / "config" / "scheduler.json"

    def _detect_runtime_root(self) -> Path:
        if self.PRODUCTION_RUNTIME.exists():
            return self.PRODUCTION_RUNTIME
        return self.DEVELOPMENT_RUNTIME

    def _load_config(self) -> dict[str, object]:
        if not self._config_path.exists():
            return {
                "mode": "daily",
                "timezone": "America/New_York",
                "hour": 7,
                "minute": 0,
                "catch_up_until_hour": 17,
                "weekdays": [1, 2, 3, 4, 5, 6, 7],
                "use_email": True,
            }

        try:
            data = json.loads(self._config_path.read_text(encoding="utf-8"))
            if isinstance(data, dict):
                return data
        except Exception:
            pass

        return {
            "mode": "daily",
            "timezone": "America/New_York",
            "hour": 7,
            "minute": 0,
            "catch_up_until_hour": 17,
            "weekdays": [1, 2, 3, 4, 5, 6, 7],
            "use_email": True,
        }

    def _is_due_today(self, today: date, config: dict[str, object]) -> bool:
        mode = str(config.get("mode", "daily")).lower()

        if mode == "daily":
            return True

        if mode == "monday":
            return today.weekday() == 0

        if mode == "weekdays":
            return today.weekday() < 5

        if mode == "custom":
            weekdays = config.get("weekdays", [])
            if isinstance(weekdays, list):
                normalized: list[int] = []
                for value in weekdays:
                    try:
                        normalized.append(int(value))
                    except (TypeError, ValueError):
                        continue
                return (today.weekday() + 1) in normalized
            return False

        return True

    def run_if_due(self) -> SchedulerRunResult:
        config = self._load_config()

        timezone_name = str(config.get("timezone", "America/New_York"))
        now_et = datetime.now(ZoneInfo(timezone_name))
        today = now_et.date()

        if not self._is_due_today(today, config):
            return SchedulerRunResult(
                executed=False,
                reason="not scheduled today",
            )

        hour_value = config.get("hour", 7)
        minute_value = config.get("minute", 0)
        catch_up_value = config.get("catch_up_until_hour", 17)

        scheduled_hour = int(hour_value) if isinstance(hour_value, (int, str)) else 7
        scheduled_minute = (
            int(minute_value) if isinstance(minute_value, (int, str)) else 0
        )
        catch_up_until_hour = (
            int(catch_up_value) if isinstance(catch_up_value, (int, str)) else 17
        )

        if now_et.time() < time(scheduled_hour, scheduled_minute):
            return SchedulerRunResult(
                executed=False,
                reason="before scheduled window",
            )

        if now_et.time() >= time(catch_up_until_hour, 0):
            return SchedulerRunResult(
                executed=False,
                reason="after catch-up window",
            )

        state = self._load_state()

        if state.get("last_successful_run") == today.isoformat():
            return SchedulerRunResult(
                executed=False,
                reason="already executed today",
            )

        started = datetime.now()

        orchestrator = MondayExecutionOrchestrator(
            inbox=self._inbox,
        )

        execution = orchestrator.execute(
            synchronize_gmail=bool(config.get("use_email", True)),
        )

        finished = datetime.now()

        self._save_state(
            {
                "last_successful_run": today.isoformat(),
                "last_finished_at": finished.isoformat(),
            }
        )

        report_path = self._runtime_root / "reports" / "monday_operations_report.md"
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(
            execution.monday_report,
            encoding="utf-8",
        )

        publish = DashboardPublisherService().publish(execution)

        MorningBriefingService(
            recipient="teknostrata@gmail.com",
        ).send(
            execution=execution,
            dashboard_url=publish.public_url,
        )

        return SchedulerRunResult(
            executed=True,
            reason="executed",
            started_at=started,
            finished_at=finished,
            report_path=report_path,
            dashboard_url=publish.public_url,
            success=True,
        )

    def _load_state(self) -> dict[str, str]:
        if not self._state_path.exists():
            return {}

        try:
            data = json.loads(self._state_path.read_text(encoding="utf-8"))

            if not isinstance(data, dict):
                return {}

            return {str(key): str(value) for key, value in data.items()}

        except Exception:
            return {}

    def _save_state(
        self,
        state: dict[str, str],
    ) -> None:
        self._state_path.parent.mkdir(parents=True, exist_ok=True)
        self._state_path.write_text(
            json.dumps(
                state,
                indent=2,
                sort_keys=True,
            ),
            encoding="utf-8",
        )
