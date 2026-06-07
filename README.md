# NeetCode 250 — Solutions

My solutions to the [NeetCode 250](https://neetcode.io/practice/practice/neetcode250),
solved in **Python** and organized by the [NeetCode roadmap](https://neetcode.io/roadmap).
Working through the topics in order, building one pattern at a time.

<!-- PROGRESS:START -->
**Progress: 2 / 250 solved**

| | Topic | Solved |
|---|---|---|
| ✅ | Arrays & Hashing | 1 |
| ✅ | Two Pointers | 1 |
| ⬜ | Sliding Window | 0 |
| ⬜ | Stack | 0 |
| ⬜ | Binary Search | 0 |
| ⬜ | Linked List | 0 |
| ⬜ | Trees | 0 |
| ⬜ | Heap / Priority Queue | 0 |
| ⬜ | Backtracking | 0 |
| ⬜ | Tries | 0 |
| ⬜ | Graphs | 0 |
| ⬜ | Advanced Graphs | 0 |
| ⬜ | 1-D Dynamic Programming | 0 |
| ⬜ | 2-D Dynamic Programming | 0 |
| ⬜ | Greedy | 0 |
| ⬜ | Intervals | 0 |
| ⬜ | Math & Geometry | 0 |
| ⬜ | Bit Manipulation | 0 |
| | **Total** | **2 / 250** |
<!-- PROGRESS:END -->

---

## How this repo is organized

Folders follow the roadmap order (prerequisites first), so the numeric prefixes
keep them sorted correctly on GitHub:

```
01_arrays_hashing/  →  02_two_pointers/  →  03_sliding_window/  →  ...  →  18_bit_manipulation/
```

Each solution file is named `<leetcode_number>_<slug>.py` (e.g. `0001_two_sum.py`)
and starts with a header that records the problem link, the **pattern** that
unlocked it, and the time/space complexity:

```python
# 1. Two Sum
# https://leetcode.com/problems/two-sum/
# Pattern: One-pass hash map storing complements as we scan
# Time: O(n)   Space: O(n)
```

The `Pattern:` line is the point — re-reading those lines later is how the
roadmap turns into pattern recognition instead of memorized answers.

## Daily workflow

```bash
# 1. copy the template into the right topic folder
cp _template.py 01_arrays_hashing/0217_contains_duplicate.py

# 2. solve it, fill in the header

# 3. refresh the progress tracker
python update_readme.py

# 4. commit one problem at a time (keeps the contribution graph honest)
git add .
git commit -m "Add Contains Duplicate (arrays & hashing)"
git push
```

## Updating progress

`update_readme.py` scans every topic folder, counts the `.py` solutions
(ignoring `_template.py`), and rewrites the table above. Just run:

```bash
python update_readme.py
```

## Roadmap topics

1. Arrays & Hashing
2. Two Pointers
3. Sliding Window
4. Stack
5. Binary Search
6. Linked List
7. Trees
8. Heap / Priority Queue
9. Backtracking
10. Tries
11. Graphs
12. Advanced Graphs
13. 1-D Dynamic Programming
14. 2-D Dynamic Programming
15. Greedy
16. Intervals
17. Math & Geometry
18. Bit Manipulation
