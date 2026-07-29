from collections.abc import Mapping
from dataclasses import dataclass, field


@dataclass
class ExtractedData:
    source_file: str
    fields: Mapping[str, object] = field(default_factory=dict)
