from pathlib import Path

PACKAGE = Path("updates/packages/MF-102.0/files/src/meridianforge/domain")


def write(path: Path, content: str):
    path.write_text(content.strip() + "\n", encoding="utf-8")
    print(f"UPDATED: {path}")


def main():

    write(
        PACKAGE / "opportunity_status.py",
        """
from enum import StrEnum


class OpportunityStatus(StrEnum):
    NEW = "NEW"
    ANALYZING = "ANALYZING"
    ANALYZED = "ANALYZED"
    WATCHLIST = "WATCHLIST"
    REJECTED = "REJECTED"
    CLOSED = "CLOSED"
""",
    )

    write(
        PACKAGE / "source.py",
        """
from dataclasses import asdict, dataclass
from enum import StrEnum


class SourceType(StrEnum):
    PDF = "PDF"
    URL = "URL"
    EMAIL = "EMAIL"
    XLSX = "XLSX"
    CSV = "CSV"
    MANUAL = "MANUAL"


@dataclass
class Source:
    source_type: SourceType
    location: str

    def validate(self) -> bool:
        if not self.location:
            raise ValueError("Source location required")
        return True

    def to_dict(self) -> dict:
        data = asdict(self)
        data["source_type"] = self.source_type.value
        return data
""",
    )

    print()
    print("MF-102.0.5 RUFF FIX COMPLETE")


if __name__ == "__main__":
    main()