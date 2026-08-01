from __future__ import annotations

from pathlib import Path

from meridianforge.intake.pipeline import process_file

ROOT = Path("samples/stress_test")

results: list[tuple[str, str, float, str]] = []

for file_path in sorted(ROOT.rglob("*")):
    if not file_path.is_file():
        continue

    if file_path.name == ".gitkeep":
        continue

    try:
        opportunity = process_file(file_path)
        results.append(
            (
                file_path.name,
                "PASS",
                float(getattr(opportunity, "confidence", 0.0)),
                "",
            )
        )
    except Exception as exc:
        results.append(
            (
                file_path.name,
                "FAIL",
                0.0,
                str(exc),
            )
        )

print()
print("MERIDIANFORGE INTAKE STRESS TEST")
print("=" * 60)
print(f"Files tested: {len(results)}")
print()

for name, status, confidence, error in results:
    print(f"{status:5} | {name:30} | confidence={confidence:.2f}")
    if error:
        print(f"      {error}")

print()
passed = sum(1 for _, status, _, _ in results if status == "PASS")
print(f"Passed: {passed}/{len(results)}")
