from typing import Any


class PropertyValidator:

    REQUIRED_FIELDS = [
        "address",
        "purchase_price",
    ]

    def validate(
        self,
        record: dict[str, Any],
    ) -> bool:

        for field in self.REQUIRED_FIELDS:

            if not record.get(field):
                return False

        return True
