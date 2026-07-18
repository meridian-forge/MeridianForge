from dataclasses import dataclass, field


@dataclass
class ValidationResult:

    opportunity_file: str

    missing_fields: list[str] = field(default_factory=list)

    notes: list[str] = field(default_factory=list)
