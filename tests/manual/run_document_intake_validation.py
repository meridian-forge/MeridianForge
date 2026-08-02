from pathlib import Path

from meridianforge.intake.pipeline import process_file

ROOT = Path("samples/stress_test")

SUPPORTED = {".pdf", ".docx", ".txt", ".xlsx", ".csv"}

results = []

for file_path in sorted(ROOT.rglob("*")):
    if not file_path.is_file():
        continue

    if file_path.name == ".gitkeep":
        continue

    if file_path.suffix.lower() not in SUPPORTED:
        continue

    try:
        opportunity = process_file(file_path)

        field_count = len(getattr(opportunity, "fields", {}))

        results.append(
            (
                file_path.name,
                "PASS",
                field_count,
                float(getattr(opportunity, "confidence", 0.0)),
                "",
            )
        )

    except Exception as exc:
        results.append(
            (
                file_path.name,
                "FAIL",
                0,
                0.0,
                str(exc),
            )
        )

print()
print("MERIDIANFORGE DOCUMENT INTAKE VALIDATION")
print("=" * 72)
print()

for name, status, fields, confidence, error in results:
    print(f"{status:5} | {name:30} | fields={fields:2d} | confidence={confidence:.2f}")

    if error:
        print(f"      {error}")

print()

passed = sum(1 for _, status, _, _, _ in results if status == "PASS")

print(f"Passed: {passed}/{len(results)}")
