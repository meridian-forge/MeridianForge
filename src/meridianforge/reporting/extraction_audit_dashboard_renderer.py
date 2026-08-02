"""
Extraction audit dashboard renderer.

MF-513.3.2

Renders extraction audit dashboard metrics into a human-readable
Markdown report suitable for Monday operations and validation reviews.
"""

from __future__ import annotations

from meridianforge.services.extraction_audit_dashboard import (
    ExtractionAuditDashboard,
)


class ExtractionAuditDashboardRenderer:
    """
    Render extraction audit dashboard summaries.
    """

    @staticmethod
    def render(
        dashboard: ExtractionAuditDashboard,
    ) -> str:
        """
        Render dashboard metrics as Markdown.
        """

        return (
            "# Extraction Audit Dashboard\n\n"
            f"- Total Records: {dashboard.total_records}\n"
            f"- Accepted: {dashboard.accepted}\n"
            f"- Review: {dashboard.review}\n"
            f"- Rejected: {dashboard.rejected}\n"
            f"- Average Confidence: {dashboard.average_confidence:.2f}\n"
        )
