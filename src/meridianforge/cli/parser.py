"""
Meridian Forge CLI argument parser.
"""

import argparse


def build_parser() -> argparse.ArgumentParser:
    """
    Build command parser.
    """

    parser = argparse.ArgumentParser(
        prog="meridianforge",
        description="Meridian Forge Investment Analysis Platform",
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
    )

    monday = subparsers.add_parser(
        "monday",
        help="Run Monday investment workflow",
    )

    monday.add_argument(
        "--file",
        help="Property input CSV/XLSX file",
    )

    acquisition = subparsers.add_parser(
        "acquisition",
        help="Run acquisition intelligence workflow",
    )

    acquisition_sub = acquisition.add_subparsers(
        dest="acquisition_command",
        required=True,
    )

    analyze = acquisition_sub.add_parser(
        "analyze",
        help="Analyze acquisition opportunity",
    )

    analyze.add_argument(
        "--file",
        required=True,
        help="Opportunity input file",
    )

    investor_package = subparsers.add_parser(
        "investor-package",
        help="Generate investor package",
    )

    investor_package.add_argument(
        "--package-id",
        required=True,
    )

    investor_package.add_argument(
        "--property-name",
        required=True,
    )

    investor_package.add_argument(
        "--recommendation",
        required=True,
    )

    investor_package.add_argument(
        "--confidence",
        type=float,
        required=True,
    )

    investor_package.add_argument(
        "--output",
        required=True,
    )

    subparsers.add_parser(
        "version",
        help="Show Meridian Forge version",
    )

    return parser
