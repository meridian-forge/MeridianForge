from __future__ import annotations

from meridianforge.services.gmail_acquisition_execution_service import (
    GmailAcquisitionExecutionResult,
)
from meridianforge.services.gmail_monday_dashboard_service import (
    GmailMondayDashboardService,
)


def test_build_dashboard() -> None:
    service = GmailMondayDashboardService()

    dashboard = service.build_dashboard(
        GmailAcquisitionExecutionResult(
            analyzed_opportunities=3,
            source="gmail",
        )
    )

    assert "MeridianForge Gmail Monday Dashboard" in dashboard
    assert "Analyzed opportunities: 3" in dashboard
    assert "Source: gmail" in dashboard
