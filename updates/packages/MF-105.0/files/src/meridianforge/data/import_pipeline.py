from typing import Any

from meridianforge.data.loader import (
    PropertyLoader,
)

from meridianforge.data.normalizer import (
    PropertyNormalizer,
)

from meridianforge.data.validator import (
    PropertyValidator,
)


class ImportPipeline:

    def __init__(self) -> None:

        self.loader = PropertyLoader()
        self.normalizer = PropertyNormalizer()
        self.validator = PropertyValidator()

    def run(
        self,
        records: list[dict[str, Any]],
    ) -> list[dict[str, Any]]:

        output = []

        for record in self.loader.load(records):

            normalized = self.normalizer.normalize(
                record
            )

            if self.validator.validate(
                normalized
            ):
                output.append(
                    normalized
                )

        return output
