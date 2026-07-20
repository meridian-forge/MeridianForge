from meridianforge.cli.parser import build_parser
from meridianforge.cli.monday_command import run_monday
from meridianforge.cli.acquisition import run_acquisition


def main() -> None:

    parser = build_parser()

    args = parser.parse_args()

    if args.command == "monday":
        run_monday(args)

    elif args.command == "acquisition":
        run_acquisition(args)

    elif args.command == "version":
        print("MeridianForge v0.10.0")


if __name__ == "__main__":
    main()
