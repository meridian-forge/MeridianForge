"""
Extraction audit report generator.

MF-513.4

Builds a Markdown extraction audit report that can be attached to
Monday operations output and future investor-facing dashboards.
"""

from __future__ import annotations

from meridianforge.reporting.extraction_audit_dashboard_renderer import (
    ExtractionAuditDashboardRenderer,
)
from meridianforge.services.extraction_audit_dashboard import (
    ExtractionAuditDashboardService,
)


class ExtractionAuditReport:
    """
    Generate extraction audit reports for operations workflows.
    """

    def __init__(
        self,
        dashboard_service: ExtractionAuditDashboardService | None = None,
    ) -> None:
        self._dashboard_service = (
            dashboard_service or ExtractionAuditDashboardService()
        )

    def generate(self) -> str:
        """
        Generate a Markdown extraction audit report.
        """

        dashboard = self._dashboard_service.build_dashboard()

        return ExtractionAuditDashboardRenderer.render(
            dashboard,
        )
