from __future__ import annotations

import subprocess
from dataclasses import dataclass
from pathlib import Path

from meridianforge.reporting.dashboard_renderer import (
    DashboardRenderer,
    build_dashboard_model,
)
from meridianforge.services.monday_execution_orchestrator import (
    MondayExecutionResult,
)


@dataclass(frozen=True, slots=True)
class DashboardPublishResult:
    published: bool
    dashboard_path: Path
    public_url: str
    commit_sha: str | None = None


class DashboardPublisherService:
    """
    Publish the MeridianForge dashboard to the GitHub Pages repository.
    Rendering is delegated to DashboardRenderer; this service only writes,
    commits, and pushes dashboard content.
    """

    DASHBOARD_REPO = Path.home() / "Documents" / "MeridianDashboard"
    PUBLIC_URL = "https://meridian-forge.github.io/meridian-dashboard/"

    def publish(
        self,
        execution: MondayExecutionResult,
    ) -> DashboardPublishResult:
        repo = self.DASHBOARD_REPO
        repo.mkdir(parents=True, exist_ok=True)

        opportunities = [
            f"{o.city}, {o.state}"
            for o in execution.operations.normalized_opportunities
        ]

        model = build_dashboard_model(
            gmail_synchronized=execution.gmail_synchronized,
            processed_count=execution.operations.artifacts_processed,
            opportunities=opportunities,
            audit_report=execution.operations.audit_report,
        )

        html = DashboardRenderer().render(model)

        dashboard_path = repo / "index.html"
        dashboard_path.write_text(
            html,
            encoding="utf-8",
        )

        self._git(["add", "index.html"], repo)

        status = self._git(["status", "--porcelain"], repo)
        if not status.stdout.strip():
            sha = self._git(["rev-parse", "--short", "HEAD"], repo).stdout.strip()
            return DashboardPublishResult(
                published=False,
                dashboard_path=dashboard_path,
                public_url=self.PUBLIC_URL,
                commit_sha=sha,
            )

        self._git(["commit", "-m", "Dashboard update"], repo)
        self._git(["push", "origin", "main"], repo)

        sha = self._git(["rev-parse", "--short", "HEAD"], repo).stdout.strip()

        return DashboardPublishResult(
            published=True,
            dashboard_path=dashboard_path,
            public_url=self.PUBLIC_URL,
            commit_sha=sha,
        )

    def _git(
        self,
        args: list[str],
        cwd: Path,
    ) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            ["git", *args],
            cwd=cwd,
            check=True,
            capture_output=True,
            text=True,
        )
