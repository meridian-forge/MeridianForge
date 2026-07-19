import sys

from meridianforge.cli.monday import (
    MondayWorkflow,
)
from meridianforge.reporting.exporter import (
    ReportExporter,
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

        print("Generating investment brief...")

        MondayWorkflow(ReportExporter())

        print("Workflow engine initialized.")

        print("Status: READY")

    else:
        print(f"Unknown command: {command}")


if __name__ == "__main__":
    main()
