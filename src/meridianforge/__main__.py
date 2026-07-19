import sys

from meridianforge.cli.monday_command import (
    run_monday,
)


def main() -> None:
    """
    Meridian Forge command-line entry point.
    """

    if len(sys.argv) < 2:
        print("Usage: python -m meridianforge monday")
        return

    command = sys.argv[1]

    if command == "monday":

        print("====================================")
        print("Meridian Forge Monday Workflow")
        print("====================================")

        print("Running opportunity analysis...")

        output = run_monday()

        print(f"Dashboard generated: {output}")

        print("Status: READY")

        print("Status: COMPLETE")

    else:
        print(f"Unknown command: {command}")


if __name__ == "__main__":
    main()
