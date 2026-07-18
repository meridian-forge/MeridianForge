import json
from typing import Any


class ReportExporter:

    def to_json(
        self,
        report: dict[str, Any],
    ) -> str:

        return json.dumps(
            report,
            indent=2,
        )
