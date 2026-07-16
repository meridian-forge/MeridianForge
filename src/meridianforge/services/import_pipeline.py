"""
Intelligent import pipeline.

Coordinates field detection, normalization,
mapping memory, confidence scoring, and result generation.
"""

from meridianforge.intelligence.confidence_engine import (
    ConfidenceEngine,
)
from meridianforge.intelligence.field_detector import (
    FieldDetector,
)
from meridianforge.intelligence.mapping_memory import (
    MappingMemory,
)
from meridianforge.models.domain.normalized_asset import (
    NormalizedAsset,
)
from meridianforge.models.results.import_warning import (
    ImportWarning,
)
from meridianforge.models.results.pipeline_result import (
    PipelineResult,
)
from meridianforge.normalization.normalizer import (
    Normalizer,
)


class ImportPipeline:
    """
    Orchestrates intelligent data normalization.
    """

    def __init__(
        self,
        mapping_memory: MappingMemory | None = None,
    ) -> None:
        self.mapping_memory = mapping_memory or MappingMemory()

    def process(
        self,
        records: list[dict[str, object]],
        asset_type: str = "UNKNOWN",
    ) -> PipelineResult:
        """
        Process raw records into normalized assets.
        """

        assets: list[dict[str, object]] = []

        warnings: list[ImportWarning] = []

        confidence_inputs = []

        for record in records:

            mappings = FieldDetector.detect(list(record.keys()))

            if not mappings:
                warnings.append(
                    ImportWarning(
                        field_name="unknown",
                        message="No recognized fields found.",
                        confidence=0.0,
                    )
                )

                continue

            normalized_asset: NormalizedAsset = Normalizer.normalize(
                record,
                mappings,
                asset_type,
            )

            assets.append(normalized_asset.attributes)

            confidence_inputs = mappings

            for mapping in mappings:
                self.mapping_memory.record_success(
                    mapping.source_field,
                    mapping.target_field,
                )

        confidence = ConfidenceEngine.calculate(
            confidence_inputs,
            self.mapping_memory,
        )

        return PipelineResult(
            assets=assets,
            confidence=confidence,
            warnings=warnings,
        )
