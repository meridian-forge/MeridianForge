from pathlib import Path

from meridianforge.cli.monday_command import run_monday
from meridianforge.cli.parser import build_parser


def load_version() -> str:
    """
    Load MeridianForge version.
    """

    version_file = Path("VERSION")

    if version_file.exists():
        return version_file.read_text(
            encoding="utf-8",
        ).strip()

    return "unknown"


def main() -> None:
    """
    MeridianForge CLI entry point.
    """

    parser = build_parser()

    args = parser.parse_args()

    if args.command == "version":
        print(f"MeridianForge {load_version()}")
        return

    if args.command == "monday":
        run_monday()
        return


if __name__ == "__main__":
    main()
