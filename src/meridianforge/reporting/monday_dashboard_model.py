from dataclasses import dataclass
from datetime import date
from pathlib import Path


@dataclass(slots=True)
class MondayDashboard:

    run_date: date

    total_opportunities: int

    buy_count: int

    watch_count: int

    pass_count: int

    average_score: float

    highest_score: float

    top_property: str

    reports_generated: int

    archive_location: Path
