"""
Intelligent import pipeline.

Coordinates field detection, normalization,
mapping memory, unknown field learning,
and mapping suggestions.
"""

from meridianforge.intelligence.field_detector import (
    FieldDetector,
)
from meridianforge.intelligence.mapping_memory import (
    MappingMemory,
)
from meridianforge.intelligence.mapping_suggester import (
    MappingSuggester,
)
from meridianforge.intelligence.unknown_field_memory import (
    UnknownFieldMemory,
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
        unknown_memory: UnknownFieldMemory | None = None,
    ) -> None:

        self.mapping_memory = mapping_memory or MappingMemory()

        self.unknown_memory = unknown_memory or UnknownFieldMemory()

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

        confidence_scores: list[float] = []

        for record in records:

            fields = list(record.keys())

            mappings = FieldDetector.detect(fields)

            if not mappings:

                for field in fields:

                    self.unknown_memory.record(
                        field,
                        fields,
                    )

                    suggestion = MappingSuggester.suggest(
                        field,
                        fields,
                    )

                    warnings.append(
                        ImportWarning(
                            field_name=field,
                            message=("Field not recognized."),
                            confidence=(suggestion.confidence if suggestion else 0.0),
                            suggested_mapping=(
                                suggestion.target_field if suggestion else None
                            ),
                            suggestion_reason=(
                                suggestion.reason if suggestion else None
                            ),
                        )
                    )

                continue

            normalized_asset: NormalizedAsset = Normalizer.normalize(
                record,
                mappings,
                asset_type,
            )

            assets.append(normalized_asset.attributes)

            for mapping in mappings:

                confidence_scores.append(mapping.confidence)

                self.mapping_memory.record_success(
                    mapping.source_field,
                    mapping.target_field,
                )

        confidence = 0.0

        if confidence_scores:

            confidence = sum(confidence_scores) / len(confidence_scores)

        return PipelineResult(
            assets=assets,
            confidence=confidence,
            warnings=warnings,
        )
