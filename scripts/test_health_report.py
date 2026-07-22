"""
MeridianForge Test Health Scanner

MF-302.5 Architecture Stabilization

Generates:
- reports/test_health_report.md
- reports/architecture_health.json
"""

from pathlib import Path
import json


ROOT = Path(".")
SRC = ROOT / "src" / "meridianforge"
TESTS = ROOT / "tests"
REPORTS = ROOT / "reports"


CORE_TARGETS = [
    "InvestmentPipeline",
    "AcquisitionOrchestrator",
    "RealEstateAdapter",
    "UnderwritingEngine",
    "DealRankingEngine",
    "DealScoringEngine",
]


def collect_python_files(path: Path):
    if not path.exists():
        return []

    return [
        p
        for p in path.rglob("*.py")
        if "__pycache__" not in str(p)
    ]


def duplicate_names(files):
    mapping = {}

    for file in files:
        mapping.setdefault(file.name, []).append(str(file))

    return {
        name: paths
        for name, paths in mapping.items()
        if len(paths) > 1
    }


def count_tests():
    functions = 0

    for file in collect_python_files(TESTS):
        try:
            text = file.read_text()
            functions += text.count("def test_")
        except Exception:
            pass

    return functions


def find_target_references(name):

    matches = []

    for file in collect_python_files(SRC):

        try:
            text = file.read_text()

            if name in text:
                matches.append(str(file))

        except Exception:
            pass

    return matches


def test_area_summary():

    areas = [
        "intake",
        "analysis",
        "ranking",
        "scoring",
        "reporting",
        "services",
        "workflows",
        "e2e",
        "cli",
    ]

    result = {}

    for area in areas:

        folder = TESTS / area

        if folder.exists():
            result[area] = len(
                list(folder.glob("test_*.py"))
            )
        else:
            result[area] = "root-level"

    return result


def generate():

    REPORTS.mkdir(exist_ok=True)

    src_files = collect_python_files(SRC)
    test_files = collect_python_files(TESTS)

    health = {

        "production_modules": len(src_files),

        "test_modules": len(test_files),

        "test_functions": count_tests(),

        "duplicate_test_names":
            duplicate_names(test_files),

        "duplicate_production_names":
            duplicate_names(src_files),

        "test_distribution":
            test_area_summary(),

        "core_targets": {},

    }


    for target in CORE_TARGETS:

        health["core_targets"][target] = {
            "references":
                find_target_references(target)
        }


    json_path = REPORTS / "architecture_health.json"

    json_path.write_text(
        json.dumps(
            health,
            indent=4,
        )
    )


    md = []

    md.append(
        "# MeridianForge Test Health Report\n"
    )

    md.append(
        "## Summary\n"
    )

    md.append(
        f"""
Production modules:
{health['production_modules']}

Test modules:
{health['test_modules']}

Test functions:
{health['test_functions']}
"""
    )


    md.append(
        "\n## Test Distribution\n"
    )

    for area, count in health["test_distribution"].items():

        md.append(
            f"- {area}: {count}"
        )


    md.append(
        "\n\n## Duplicate Production Files\n"
    )

    for name in health["duplicate_production_names"]:

        md.append(
            f"- {name}"
        )


    md.append(
        "\n\n## Duplicate Test Files\n"
    )

    for name in health["duplicate_test_names"]:

        md.append(
            f"- {name}"
        )


    md.append(
        "\n\n## Core Architecture Targets\n"
    )


    for target, data in health["core_targets"].items():

        md.append(
            f"""
### {target}

Referenced in:

"""
        )

        for ref in data["references"]:
            md.append(
                f"- {ref}"
            )


    report_path = REPORTS / "test_health_report.md"

    report_path.write_text(
        "\n".join(md)
    )


    print("=====================================")
    print(" MeridianForge Test Health Report")
    print("=====================================")
    print()
    print(f"Production modules: {health['production_modules']}")
    print(f"Test modules:      {health['test_modules']}")
    print(f"Test functions:    {health['test_functions']}")
    print()
    print("Generated:")
    print(report_path)
    print(json_path)


if __name__ == "__main__":
    generate()
