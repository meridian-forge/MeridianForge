import sys
from pathlib import Path

from meridianforge.cli.monday_command import (
    run_monday,
)


def main() -> None:
    """
    Meridian Forge command-line entry point.
    """

    if len(sys.argv) < 2:
        print("Usage: python -m meridianforge monday [--file properties.csv]")
        return

    command = sys.argv[1]

    if command == "monday":

        file_path: Path | None = None

        if len(sys.argv) >= 3:

            if sys.argv[2] == "--file":

                if len(sys.argv) < 4:
                    print("Missing file path after --file")
                    return

                file_path = Path(sys.argv[3])

            else:
                print(f"Unknown option: {sys.argv[2]}")
                return

        print("====================================")
        print("Meridian Forge Monday Workflow")
        print("====================================")

        print("Running opportunity analysis...")

        output = run_monday(file_path)

        print(f"Dashboard generated: {output}")

        print("Status: READY")

        print("Status: COMPLETE")

    else:
        print(f"Unknown command: {command}")


if __name__ == "__main__":
    main()
