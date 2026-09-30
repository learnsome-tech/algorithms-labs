# m06l03-02 · Recursive DFS: visit order through a directed graph

**Lesson:** [Depth-First Search, Cycles And Topological Order](https://learnsome.tech/learn/algorithms-course/m06l03) (lesson 6.3, module 6: Graphs And Their Algorithms) · Pro  
**Check:** Graded

## Goal

You can implement recursive DFS, detect a cycle in a directed graph using colour marking, and sort a dependency graph into valid execution order using Kahn's algorithm.

In the lesson: The directed graph has six vertices connected in a tree-like pattern with a shared sink. Starting at A, DFS immediately dives into A's first neighbour, B. From B it goes to D, which has no outgoing edges, so the call returns. Back at B, it tries E, which leads to F. After visiting F the call unwinds back to B, then to A, and then DFS finally processes A's second neighbour, C. C also leads to F, but F is already in the visited set, so that branch is skipped. The visit order, printed as each vertex is first reached, shows the depth-first pattern: one entire branch, A through B D E F, is exhausted before C is visited. The visited set initialized lazily on first call prevents creating a new set on every recursive call.

## Files

- [`starter/dfs_visit.py`](starter/dfs_visit.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l03/m06l03-02/starter`
2. Read `dfs_visit.py` the way the lesson builds it:
   - Lines 1–2: directed graph
   - Lines 3–11: recursive call
   - Lines 12–13: visit order
3. Run it: `python3 dfs_visit.py`.
4. Check it from the repository root: `./check m06l03-02`.

## Expected output

```text
visit A
visit B
visit D
visit E
visit F
visit C
```

## How to check

`./check m06l03-02` copies `starter/` into a scratch directory and runs `python3 dfs_visit.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m06l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
