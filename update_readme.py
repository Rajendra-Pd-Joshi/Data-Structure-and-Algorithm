#!/usr/bin/env python3
"""
Regenerate README.md progress tracker by scanning topic folders.

Usage:
    python update_readme.py

Counts every .py file in each NN_topic/ folder (ignoring _template.py and
files starting with '_'), then rewrites the progress table in README.md
between the <!-- PROGRESS:START --> and <!-- PROGRESS:END --> markers.
"""

import re
from pathlib import Path

ROOT = Path(__file__).parent

# Folder prefix -> nice display name
DISPLAY = {
    "01_arrays_hashing": "Arrays & Hashing",
    "02_two_pointers": "Two Pointers",
    "03_sliding_window": "Sliding Window",
    "04_stack": "Stack",
    "05_binary_search": "Binary Search",
    "06_linked_list": "Linked List",
    "07_trees": "Trees",
    "08_heap_priority_queue": "Heap / Priority Queue",
    "09_backtracking": "Backtracking",
    "10_tries": "Tries",
    "11_graphs": "Graphs",
    "12_advanced_graphs": "Advanced Graphs",
    "13_1d_dynamic_programming": "1-D Dynamic Programming",
    "14_2d_dynamic_programming": "2-D Dynamic Programming",
    "15_greedy": "Greedy",
    "16_intervals": "Intervals",
    "17_math_geometry": "Math & Geometry",
    "18_bit_manipulation": "Bit Manipulation",
}


def count_solutions(folder: Path) -> int:
    if not folder.is_dir():
        return 0
    return sum(
        1
        for f in folder.glob("*.py")
        if not f.name.startswith("_")
    )


def bar(done: int, total: int = 25, width: int = 14) -> str:
    # rough visual bar; total is a soft per-topic reference, not a hard target
    pct = min(done / total, 1.0) if total else 0
    filled = round(pct * width)
    return "█" * filled + "░" * (width - filled)


def main() -> None:
    rows = []
    total_solved = 0
    for prefix, name in DISPLAY.items():
        n = count_solutions(ROOT / prefix)
        total_solved += n
        check = "✅" if n > 0 else "⬜"
        rows.append(f"| {check} | {name} | {n} |")

    table = ["| | Topic | Solved |", "|---|---|---|"]
    table.extend(rows)
    table.append(f"| | **Total** | **{total_solved} / 250** |")

    block = (
        "<!-- PROGRESS:START -->\n"
        f"**Progress: {total_solved} / 250 solved**\n\n"
        + "\n".join(table)
        + "\n<!-- PROGRESS:END -->"
    )

    readme = ROOT / "README.md"
    text = readme.read_text(encoding="utf-8")
    new_text = re.sub(
        r"<!-- PROGRESS:START -->.*?<!-- PROGRESS:END -->",
        block,
        text,
        flags=re.DOTALL,
    )
    readme.write_text(new_text, encoding="utf-8")
    print(f"README updated. Total solved: {total_solved} / 250")


if __name__ == "__main__":
    main()
