from pathlib import Path

SUPPORTED_EXTENSIONS = {
    ".xlsx",
    ".xls",
    ".csv",
    ".pdf",
    ".docx",
    ".txt",
    ".rtf",
}


def scan_directory(path: str) -> list[Path]:
    """
    Scan a directory recursively for supported
    investment opportunity artifacts.
    """

    directory = Path(path)

    if not directory.exists():
        return []

    return [
        file
        for file in directory.rglob("*")
        if file.is_file()
        and file.suffix.lower() in SUPPORTED_EXTENSIONS
    ]
