# m06l01-04 · Space: sparse versus dense graphs

**Lesson:** [Representing A Graph: Matrix Or Adjacency List](https://learnsome.tech/learn/algorithms-course/m06l01) (lesson 6.1, module 6: Graphs And Their Algorithms) · Pro  
**Check:** Graded

## Goal

You can represent a graph as either an adjacency list or a two-dimensional matrix, state the memory cost of each, explain when to prefer one over the other, and encode directed and weighted edges.

In the lesson: Let us put numbers to the space comparison. For five vertices and five edges, the matrix needs twenty-five cells while the adjacency list needs only fifteen entries. The gap widens as graphs grow. Scale to one thousand vertices and three thousand edges - a moderately sparse graph - and the matrix demands one million cells, while the adjacency list stores just seven thousand. Road networks, social graphs, and dependency graphs are all sparse: each vertex connects to only a handful of others. For those cases the list saves enormous memory. Dense graphs, where nearly every pair of vertices is connected, are less common in practice; the matrix's constant-time edge lookup becomes worthwhile only when the edge density is high.

## Files

- [`starter/shell-space-sparse-versus-dense-graphs.py`](starter/shell-space-sparse-versus-dense-graphs.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l01/m06l01-04/starter`
2. Read `shell-space-sparse-versus-dense-graphs.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   v, e = 5, 5
   v * v
   v + 2 * e
   v, e = 1000, 3000
   v * v
   v + 2 * e
   ```
4. Run it: `python3 -i < shell-space-sparse-versus-dense-graphs.py`.
5. Check it from the repository root: `./check m06l01-04`.

## Expected output

```text
25
15
1000000
7000
```

## How to check

`./check m06l01-04` copies `starter/` into a scratch directory and runs `python3 -i < shell-space-sparse-versus-dense-graphs.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m06l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
