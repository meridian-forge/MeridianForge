"""
Meridian Forge CLI argument parser.
"""

import argparse


def build_parser() -> argparse.ArgumentParser:
    """
    Build command line parser.
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

    subparsers.add_parser(
        "version",
        help="Show Meridian Forge version",
    )

    return parser
