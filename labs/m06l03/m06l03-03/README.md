# m06l03-03 · Cycle detection with three-colour DFS marking

**Lesson:** [Depth-First Search, Cycles And Topological Order](https://learnsome.tech/learn/algorithms-course/m06l03) (lesson 6.3, module 6: Graphs And Their Algorithms) · Pro  
**Check:** Graded

## Goal

You can implement recursive DFS, detect a cycle in a directed graph using colour marking, and sort a dependency graph into valid execution order using Kahn's algorithm.

In the lesson: Three colours track each vertex through its lifetime in the search. White means unvisited. Gray means the vertex is on the current search path - the recursive call has started but not returned. Black means the vertex is fully processed and all its descendants have been explored. Colour each vertex gray when DFS enters it, and black when DFS leaves it. A directed cycle exists when DFS encounters a gray vertex: that means we have followed a path from the gray vertex and arrived back at it, forming a back edge. The dag graph has no such back edge, so the detector returns False. The cyclic graph has A, B, C, and C points back to A which is still gray when C is being processed. Detecting back edges is the correct criterion for directed cycles; undirected graphs use a different check.

## Files

- [`starter/cycle_detect.py`](starter/cycle_detect.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l03/m06l03-03/starter`
2. Read `cycle_detect.py` the way the lesson builds it:
   - Lines 1: three colours
   - Lines 2–12: colour each vertex
   - Lines 13–17: back edge
3. Run it: `python3 cycle_detect.py`.
4. Check it from the repository root: `./check m06l03-03`.

## Expected output

```text
dag has cycle: False
cyclic has cycle: True
```

## How to check

`./check m06l03-03` copies `starter/` into a scratch directory and runs `python3 cycle_detect.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m06l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
