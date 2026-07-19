from pathlib import Path


path = Path(".gitignore")

text = path.read_text()


old = """# ======================================
# Meridian Forge Runtime Workspace
# ======================================

runtime/*
!runtime/
!runtime/outputs/
"""


new = """# ======================================
# Meridian Forge Runtime Workspace
# ======================================

runtime/*
!runtime/
!runtime/outputs/
runtime/outputs/*
!runtime/outputs/.gitkeep
"""


if new in text:
    print("Runtime ignore rules already fixed.")
    raise SystemExit(0)


if old not in text:
    raise SystemExit(
        "Expected runtime block not found."
    )


text = text.replace(
    old,
    new,
)


path.write_text(
    text,
)


print(
    "Runtime ignore rules fixed."
)
