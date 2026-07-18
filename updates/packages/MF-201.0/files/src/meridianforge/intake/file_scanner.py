from pathlib import Path


SUPPORTED_EXTENSIONS = {
    ".xlsx",
    ".xls",
    ".csv",
    ".pdf",
    ".json",
}


def scan_directory(path: str) -> list[Path]:
    directory = Path(path)

    if not directory.exists():
        return []

    return [
        file
        for file in directory.rglob("*")
        if file.is_file()
        and file.suffix.lower() in SUPPORTED_EXTENSIONS
    ]
