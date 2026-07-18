import json
from pathlib import Path


class OpportunityRepository:

    def __init__(self, path="data/opportunities.json"):
        self.path = Path(path)

    def save(self, opportunity):
        self.path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        self.path.write_text(
            json.dumps(
                opportunity,
                default=lambda x: x.__dict__,
                indent=2
            )
        )

        return True
