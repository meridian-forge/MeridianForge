from pathlib import Path

from meridianforge.cli.acquisition import run_acquisition
from meridianforge.cli.monday_command import run_monday
from meridianforge.cli.parser import build_parser


def main() -> None:

    parser = build_parser()

    args = parser.parse_args()

    if args.command == "monday":
        run_monday(Path(args.file) if args.file else None)

    elif args.command == "acquisition":
        run_acquisition(args)

    elif args.command == "version":
        print("MeridianForge v0.10.0")


if __name__ == "__main__":
    main()
