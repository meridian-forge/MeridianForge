from __future__ import annotations

from meridianforge.services.gmail_acquisition_execution_service import (
    GmailAcquisitionExecutionResult,
)


class GmailMondayDashboardService:
    """
    Build a Monday dashboard from Gmail acquisition execution results.

    This produces investor-facing reporting while preserving the existing
    reporting pipeline.
    """

    def build_dashboard(
        self,
        result: GmailAcquisitionExecutionResult,
    ) -> str:
        return (
            "# MeridianForge Gmail Monday Dashboard\n\n"
            f"Source: {result.source}\n"
            f"Analyzed opportunities: {result.analyzed_opportunities}\n"
        )
