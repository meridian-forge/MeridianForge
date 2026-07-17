from pathlib import Path

FILES = {
    "src/meridianforge/domain/provider.py": """
from dataclasses import dataclass


@dataclass
class Provider:
    name: str
    contact: str | None = None

    def validate(self) -> bool:
        if not self.name:
            raise ValueError("Provider name required")
        return True
""",

    "src/meridianforge/domain/opportunity.py": """
from dataclasses import dataclass

from meridianforge.domain.opportunity_status import OpportunityStatus
from meridianforge.domain.source import Source


@dataclass
class Opportunity:
    name: str
    source: Source
    status: OpportunityStatus = OpportunityStatus.NEW

    def validate(self) -> bool:
        if not self.name:
            raise ValueError("Opportunity name required")

        self.source.validate()

        return True
""",

    "src/meridianforge/repositories/opportunity_repository.py": """
import json
from pathlib import Path
from typing import Any


class OpportunityRepository:

    def __init__(self, path: str = "data/opportunities.json") -> None:
        self.path = Path(path)

    def save(self, opportunity: Any) -> bool:
        self.path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        self.path.write_text(
            json.dumps(
                opportunity,
                default=lambda x: x.__dict__,
                indent=2,
            )
        )

        return True
""",
}


def main() -> None:
    root = Path.cwd()

    for file_path, content in FILES.items():
        target = root / file_path
        target.write_text(content.strip() + "\n", encoding="utf-8")
        print(f"UPDATED: {file_path}")

    print()
    print("MF-102.0.6 MYPY FIX COMPLETE")


if __name__ == "__main__":
    main()