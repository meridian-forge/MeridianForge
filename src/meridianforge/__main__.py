from pathlib import Path

from meridianforge.cli.monday_command import run_monday
from meridianforge.cli.parser import build_parser


def load_version() -> str:
    """
    Load Meridian Forge version from repository VERSION file.
    """

    version_file = Path("VERSION")

    if version_file.exists():
        return version_file.read_text(
            encoding="utf-8",
        ).strip()

    return "unknown"


def main() -> None:
    """
    Meridian Forge command-line entry point.
    """

    parser = build_parser()

    args = parser.parse_args()

    if args.command == "version":

        print(f"Meridian Forge {load_version()}")

        return

    if args.command == "monday":

        file_path = None

        if args.file:
            file_path = Path(args.file)

        print("====================================")
        print("Meridian Forge Monday Workflow")
        print("====================================")

        print("Running opportunity analysis...")

        print("Status: READY")

        output = run_monday(file_path)

        print(f"Dashboard generated: {output}")

        print("Status: COMPLETE")


if __name__ == "__main__":
    main()
