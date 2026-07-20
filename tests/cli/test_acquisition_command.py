from meridianforge.cli.parser import build_parser


def test_acquisition_cli_parser():

    parser = build_parser()

    args = parser.parse_args(
        [
            "acquisition",
            "analyze",
            "--file",
            "property.csv",
        ]
    )

    assert args.command == "acquisition"
    assert args.acquisition_command == "analyze"
    assert args.file == "property.csv"
