from meridianforge.cli.acquisition import run_acquisition
from meridianforge.cli.investor_package import run_investor_package
from meridianforge.cli.monday_command import run_monday
from meridianforge.cli.parser import build_parser

VERSION = "1.0.0-RC1"


def main() -> None:
    parser = build_parser()

    args = parser.parse_args()

    if args.command == "monday":
        run_monday(
            use_email=args.email,
        )

    elif args.command == "acquisition":
        run_acquisition(args)

    elif args.command == "investor-package":
        run_investor_package(args)

    elif args.command == "version":
        print(f"MeridianForge {VERSION}")


if __name__ == "__main__":
    main()
