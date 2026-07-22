from pathlib import Path
from datetime import datetime


ROOT = Path(__file__).resolve().parents[1]

SRC = ROOT / "src" / "meridianforge"
REPORT = ROOT / "reports" / "meridianforge_architecture_map.md"


LAYERS = {
    "Domain Models": [
        "models",
        "domain",
    ],
    "Engines": [
        "engine",
        "analysis",
        "scoring",
        "ranking",
    ],
    "Services": [
        "services",
    ],
    "Workflows": [
        "workflow",
        "workflows",
    ],
    "Intake / Import": [
        "intake",
        "imports",
        "importers",
        "data",
    ],
    "Reporting / Presentation": [
        "reporting",
        "presentation",
        "reports",
    ],
    "Application / CLI": [
        "application",
        "cli",
    ],
}


def find_modules(paths: list[str]) -> list[str]:
    results = []

    for path in paths:
        folder = SRC / path

        if folder.exists():
            for file in sorted(folder.rglob("*.py")):
                results.append(
                    str(file.relative_to(SRC))
                )

    return results


def build_report() -> str:
    lines = []

    lines.append("# MeridianForge Architecture Map")
    lines.append("")
    lines.append(
        f"Generated: {datetime.now().isoformat()}"
    )
    lines.append("")

    lines.append(
        """
## Architecture Direction

MeridianForge follows this dependency direction:

Domain Models
        ↓
Engines
        ↓
Services
        ↓
Workflows
        ↓
Presentation / CLI

Lower layers should not depend on higher layers.
"""
    )

    for name, paths in LAYERS.items():

        lines.append("")
        lines.append(f"## {name}")
        lines.append("")

        modules = find_modules(paths)

        if modules:
            for module in modules:
                lines.append(
                    f"- `{module}`"
                )
        else:
            lines.append(
                "- None"
            )

    lines.append("")
    lines.append(
        """
## Canonical Ownership Decisions

| Capability | Owner |
|---|---|
| Underwriting | engine |
| Deal Ranking | engine |
| Deal Scoring | engine |
| Investment Pipeline | services |
| Acquisition Flow | workflows/services |
| Reporting | reporting |
| File Intake | intake |
"""
    )

    return "\n".join(lines)


def main() -> None:
    REPORT.write_text(
        build_report(),
        encoding="utf-8",
    )

    print(
        f"Generated {REPORT}"
    )


if __name__ == "__main__":
    main()
