from pathlib import Path
import shutil


ROOT = Path(__file__).resolve().parent.parent

SOURCE = ROOT / "docs_source" / "MF101"
TARGET = ROOT / "Documentation"


def create_directories():
    folders = [
        TARGET / "Architecture",
        TARGET / "Decisions",
        TARGET / "Releases",
    ]

    for folder in folders:
        folder.mkdir(parents=True, exist_ok=True)


def copy_documents():
    if not SOURCE.exists():
        raise FileNotFoundError(
            f"Missing source documentation folder: {SOURCE}"
        )

    copied = 0

    for source_file in SOURCE.rglob("*.md"):
        relative = source_file.relative_to(SOURCE)
        destination = TARGET / relative

        destination.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        shutil.copy2(
            source_file,
            destination
        )

        print(f"COPIED: {relative}")
        copied += 1

    return copied


def main():

    print()
    print("======================================")
    print("MF-101 DOCUMENTATION GENERATOR")
    print("======================================")
    print()

    create_directories()

    count = copy_documents()

    print()
    print("======================================")
    print(f"MF-101 DOCUMENTS CREATED: {count}")
    print("======================================")
    print()


if __name__ == "__main__":
    main()