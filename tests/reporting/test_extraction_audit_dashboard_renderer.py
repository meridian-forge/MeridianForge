from meridianforge.reporting.extraction_audit_dashboard_renderer import (
    ExtractionAuditDashboardRenderer,
)
from meridianforge.services.extraction_audit_dashboard import (
    ExtractionAuditDashboard,
)


def test_renderer_outputs_markdown_dashboard() -> None:
    dashboard = ExtractionAuditDashboard(
        total_records=12,
        accepted=9,
        review=2,
        rejected=1,
        average_confidence=0.94,
    )

    output = ExtractionAuditDashboardRenderer.render(
        dashboard,
    )

    assert "# Extraction Audit Dashboard" in output
    assert "Total Records: 12" in output
    assert "Accepted: 9" in output
    assert "Review: 2" in output
    assert "Rejected: 1" in output
    assert "Average Confidence: 0.94" in output
