from typing import Any


class PropertyNormalizer:

    def normalize(
        self,
        record: dict[str, Any],
    ) -> dict[str, Any]:

        return {
            "address": record.get("address"),
            "purchase_price": float(
                record.get(
                    "price",
                    0,
                )
            ),
            "rent": float(
                record.get(
                    "rent",
                    0,
                )
            ),
        }
