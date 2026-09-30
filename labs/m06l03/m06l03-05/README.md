# m06l03-05 · Kahn's algorithm on a build-dependency graph

**Lesson:** [Depth-First Search, Cycles And Topological Order](https://learnsome.tech/learn/algorithms-course/m06l03) (lesson 6.3, module 6: Graphs And Their Algorithms) · Pro  
**Check:** Graded

## Goal

You can implement recursive DFS, detect a cycle in a directed graph using colour marking, and sort a dependency graph into valid execution order using Kahn's algorithm.

In the lesson: The dependency map lists what each step needs before it can run. The algorithm first builds a forward adjacency map and an in-degree count: the in-degree of a step is the number of prerequisites it still has outstanding. The queue starts with every step whose in-degree is zero, meaning it has no prerequisites. Only compile qualifies at the start. As each step is appended to the order, Kahn's algorithm decrements the in-degree of every step that depended on it; when a step's in-degree reaches zero it joins the queue. The valid build order shows compile first, then link and test in parallel dependency order, then package after both, and finally deploy. If the graph had a cycle, some vertices would never reach in-degree zero and would be absent from the output - a simple way to detect cycles as a side effect.

## Files

- [`starter/kahn.py`](starter/kahn.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l03/m06l03-05/starter`
2. Read `kahn.py` the way the lesson builds it:
   - Lines 1–4: dependency map
   - Lines 5–10: forward adjacency
   - Lines 11–20: valid build order
3. Run it: `python3 kahn.py`.
4. Check it from the repository root: `./check m06l03-05`.

## Expected output

```text
['compile', 'link', 'test', 'package', 'deploy']
```

## How to check

`./check m06l03-05` copies `starter/` into a scratch directory and runs `python3 kahn.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m06l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
