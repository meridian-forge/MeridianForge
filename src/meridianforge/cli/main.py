import argparse

from meridianforge.analysis.analyzer import analyze
from meridianforge.intake.pipeline import process_folder
from meridianforge.ranking.engine import rank
from meridianforge.reporting.text_report import (
    generate_text_report,
)


def run_analyze(
    folder: str,
) -> None:

    opportunities = process_folder(folder)

    results = [analyze(item) for item in opportunities]

    rankings = rank(results)

    report = generate_text_report(rankings)

    print(report.content)


def main() -> None:

    parser = argparse.ArgumentParser(
        prog="meridianforge",
    )

    subparsers = parser.add_subparsers(
        dest="command",
    )

    analyze_parser = subparsers.add_parser(
        "analyze",
    )

    analyze_parser.add_argument(
        "folder",
    )

    args = parser.parse_args()

    if args.command == "analyze":

        run_analyze(args.folder)


if __name__ == "__main__":

    main()
