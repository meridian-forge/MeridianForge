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
