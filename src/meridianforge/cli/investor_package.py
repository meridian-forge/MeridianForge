"""
Investor package CLI command.
"""

import argparse
from pathlib import Path

from meridianforge.workflows.investor_package_workflow import (
    InvestorPackageWorkflow,
)


def run_investor_package(
    args: argparse.Namespace,
) -> None:
    """
    Generate an investor package.
    """

    workflow = InvestorPackageWorkflow()

    package = workflow.generate(
        package_id=args.package_id,
        property_name=args.property_name,
        recommendation=args.recommendation,
        confidence=args.confidence,
        output_directory=Path(args.output),
    )

    print(
        f"Investor package created: {package.package_id}",
    )
