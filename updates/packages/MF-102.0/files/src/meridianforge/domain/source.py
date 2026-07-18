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
