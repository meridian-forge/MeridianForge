from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from zoneinfo import ZoneInfo


@dataclass(frozen=True, slots=True)
class DashboardMetric:
    label: str
    value: str


@dataclass(frozen=True, slots=True)
class DashboardViewModel:
    generated_at: datetime
    buy_count: int
    watch_count: int
    review_count: int
    processed_count: int
    gmail_synchronized: bool
    top_opportunity: str | None
    opportunities: list[str]
    audit_report: str


class DashboardRenderer:
    """
    Render the MeridianForge dashboard HTML from a structured view model.
    """

    def render(
        self,
        model: DashboardViewModel,
    ) -> str:
        generated = model.generated_at.astimezone(
            ZoneInfo("America/New_York")
        ).strftime("%B %d, %Y %I:%M %p ET")

        metrics = [
            DashboardMetric("BUY", str(model.buy_count)),
            DashboardMetric("WATCH", str(model.watch_count)),
            DashboardMetric("REVIEW", str(model.review_count)),
            DashboardMetric("Processed", str(model.processed_count)),
        ]

        metric_html = "".join(
            f"""
            <div class="metric">
              <div class="label">{m.label}</div>
              <div class="value">{m.value}</div>
            </div>
            """
            for m in metrics
        )

        opportunities = (
            "".join(f"<li>{item}</li>" for item in model.opportunities)
            or "<li>No opportunities processed</li>"
        )

        top = model.top_opportunity or "No top opportunity available"

        return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>MeridianForge Command Center</title>
  <style>
    :root {{
      --bg: #f4f7fb;
      --card: #ffffff;
      --text: #111827;
      --muted: #6b7280;
      --border: #e5e7eb;
      --accent: #2563eb;
    }}

    body {{
      margin: 0;
      padding: 32px;
      background: var(--bg);
      color: var(--text);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    }}

    .container {{
      max-width: 1100px;
      margin: 0 auto;
    }}

    h1 {{
      margin-bottom: 6px;
    }}

    .muted {{
      color: var(--muted);
    }}

    .grid {{
      display: grid;
      grid-template-columns: repeat(4, minmax(120px, 1fr));
      gap: 16px;
      margin: 24px 0;
    }}

    .metric {{
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 18px;
    }}

    .metric .label {{
      color: var(--muted);
      font-size: 13px;
      margin-bottom: 8px;
    }}

    .metric .value {{
      font-size: 34px;
      font-weight: 700;
    }}

    .card {{
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 22px;
      margin-top: 18px;
    }}

    .section-title {{
      margin: 0 0 14px 0;
      font-size: 20px;
    }}

    ul {{
      margin: 0;
      padding-left: 20px;
    }}

    pre {{
      white-space: pre-wrap;
      font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
      font-size: 13px;
    }}

    .status {{
      display: inline-block;
      padding: 6px 10px;
      border-radius: 999px;
      background: #ecfeff;
      color: #155e75;
      font-size: 12px;
      font-weight: 600;
    }}

    @media (max-width: 768px) {{
      .grid {{
        grid-template-columns: repeat(2, minmax(120px, 1fr));
      }}
    }}
  </style>
</head>
<body>
  <div class="container">
    <h1>MeridianForge Command Center</h1>
    <div class="muted">Generated {generated}</div>

    <div class="grid">
      {metric_html}
    </div>

    <div class="card">
      <div class="section-title">Top Opportunity</div>
      <p>{top}</p>
    </div>

    <div class="card">
      <div class="section-title">Pipeline</div>
      <ul>
        {opportunities}
      </ul>
    </div>

    <div class="card">
      <div class="section-title">System Health</div>
      <p>
        Scheduler:
        <span class="status">Healthy</span>
      </p>
      <p>
        Gmail Sync:
        <span class="status">
          {"Successful" if model.gmail_synchronized else "Pending"}
        </span>
      </p>
    </div>

    <div class="card">
      <div class="section-title">Extraction Audit</div>
      <pre>{model.audit_report}</pre>
    </div>
  </div>
</body>
</html>"""


def build_dashboard_model(
    *,
    gmail_synchronized: bool,
    processed_count: int,
    opportunities: list[str],
    audit_report: str,
) -> DashboardViewModel:
    buy = sum(1 for item in opportunities if "BUY" in item.upper())
    watch = sum(1 for item in opportunities if "WATCH" in item.upper())
    review = sum(1 for item in opportunities if "REVIEW" in item.upper())

    top = opportunities[0] if opportunities else None

    return DashboardViewModel(
        generated_at=datetime.now(ZoneInfo("America/New_York")),
        buy_count=buy,
        watch_count=watch,
        review_count=review,
        processed_count=processed_count,
        gmail_synchronized=gmail_synchronized,
        top_opportunity=top,
        opportunities=opportunities,
        audit_report=audit_report,
    )
