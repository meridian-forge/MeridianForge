"""
Import execution result model.

Represents the complete outcome of a file import
operation.
"""

from dataclasses import dataclass, field

from meridianforge.models.results.import_quality_report import (
    ImportQualityReport,
)
from meridianforge.models.results.import_warning import (
    ImportWarning,
)


@dataclass(slots=True)
class ImportExecutionResult:
    """
    Complete import execution output.
    """

    assets: list[dict[str, object]] = field(
        default_factory=list,
    )

    quality_report: ImportQualityReport | None = None

    warnings: list[ImportWarning] = field(
        default_factory=list,
    )
