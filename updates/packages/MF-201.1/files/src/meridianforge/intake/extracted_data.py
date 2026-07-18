from dataclasses import dataclass, field


@dataclass
class ExtractedData:
    source_file: str
    fields: dict[str, str] = field(default_factory=dict)
