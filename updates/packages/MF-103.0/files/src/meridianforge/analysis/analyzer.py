from typing import Any

from meridianforge.analysis.underwriting_engine import (
    UnderwritingEngine,
)


class Analyzer:

    def __init__(self) -> None:
        self.engine = UnderwritingEngine()

    def run(self, **kwargs: Any) -> Any:
        return self.engine.analyze(**kwargs)
