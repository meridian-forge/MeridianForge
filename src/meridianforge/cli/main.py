"""
Meridian Forge CLI entry point.
"""

import argparse

from meridianforge.cli.commands import (
    analyze_command,
)


def main() -> None:
    """
    Execute CLI application.
    """

    parser = argparse.ArgumentParser(
        prog="meridianforge",
        description="AI-assisted real estate underwriting platform",
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
    )

    analyze_parser = subparsers.add_parser(
        "analyze",
        help="Analyze a property JSON file",
    )

    analyze_parser.add_argument(
        "file",
        help="Path to property JSON file",
    )

    args = parser.parse_args()

    if args.command == "analyze":
        print(
            analyze_command(
                args.file,
            )
        )


if __name__ == "__main__":
    main()
