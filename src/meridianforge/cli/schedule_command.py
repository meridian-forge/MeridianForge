from __future__ import annotations

from meridianforge.services.scheduler_service import SchedulerService


def run_schedule() -> int:
    result = SchedulerService().run_if_due()

    print("MeridianForge Scheduler")
    print(f"Executed : {result.executed}")
    print(f"Reason   : {result.reason}")

    if result.executed:
        print(f"Success  : {result.success}")
        if result.report_path is not None:
            print(f"Report   : {result.report_path}")
        if result.dashboard_url is not None:
            print(f"Dashboard: {result.dashboard_url}")

    return 0


def run() -> int:
    return run_schedule()


if __name__ == "__main__":
    raise SystemExit(run_schedule())
