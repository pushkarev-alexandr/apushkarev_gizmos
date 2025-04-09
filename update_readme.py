from pathlib import Path

with open("README.md", "w", encoding="utf-8") as f:
    f.write("# Nuke gizmos\n\n")
    path = Path.cwd()
    for item in sorted(path.iterdir()):
        if item.is_dir() and not item.name.startswith('.'):
            f.write(f"### {item.name}\n")
            for sub_item in sorted(item.iterdir()):
                if sub_item.is_file() and (sub_item.name.endswith('.gizmo') or sub_item.name.endswith('.nk')):
                    f.write(f"- {sub_item.name}\n")
