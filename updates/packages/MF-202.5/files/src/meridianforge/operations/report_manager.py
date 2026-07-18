from datetime import datetime
from pathlib import Path


def create_report_directory(
    base_path: Path,
) -> Path:

    reports = base_path / "reports"

    reports.mkdir(
        exist_ok=True,
    )

    return reports


def create_report_filename(
    extension: str = "xlsx",
) -> str:

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    return (
        f"investment_review_{timestamp}.{extension}"
    )
