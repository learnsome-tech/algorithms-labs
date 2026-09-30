# m06l03-06 · Verifying the topological order

**Lesson:** [Depth-First Search, Cycles And Topological Order](https://learnsome.tech/learn/algorithms-course/m06l03) (lesson 6.3, module 6: Graphs And Their Algorithms) · Pro  
**Check:** Graded

## Goal

You can implement recursive DFS, detect a cycle in a directed graph using colour marking, and sort a dependency graph into valid execution order using Kahn's algorithm.

In the lesson: The position of compile is zero, confirming it runs first. Package is at position three. Both link and test appear at earlier positions than package, which is exactly what topological correctness requires: every prerequisite comes before the step that depends on it. Checking these index relationships is how you verify a proposed topological order by hand. In automated testing you would iterate over every edge in the dependency graph and assert that the source appears earlier than the destination. A topological order is not unique - link and test could swap positions and both would still be valid - but any valid order satisfies all dependency constraints.

## Files

- [`starter/shell-verifying-the-topological-order.py`](starter/shell-verifying-the-topological-order.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l03/m06l03-06/starter`
2. Read `shell-verifying-the-topological-order.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   order = ['compile','link','test','package','deploy']
   order.index('compile')
   order.index('package')
   order.index('link') < order.index('package')
   order.index('test') < order.index('package')
   ```
4. Run it: `python3 -i < shell-verifying-the-topological-order.py`.
5. Check it from the repository root: `./check m06l03-06`.

## Expected output

```text
0
3
True
True
```

## How to check

`./check m06l03-06` copies `starter/` into a scratch directory and runs `python3 -i < shell-verifying-the-topological-order.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m06l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
