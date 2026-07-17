from dataclasses import dataclass


@dataclass
class Provider:
    name: str
    contact: str | None = None

    def validate(self) -> bool:
        if not self.name:
            raise ValueError("Provider name required")
        return True
