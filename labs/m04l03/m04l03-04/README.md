# m04l03-04 · The bisect module in the Shell

**Lesson:** [Binary Search And Its Invariant](https://learnsome.tech/learn/algorithms-course/m04l03) (lesson 4.3, module 4: Sorting And Searching) · Pro  
**Check:** Graded

## Goal

You can implement iterative binary search with a loop invariant, identify and fix common off-by-one errors, use the bisect module for sorted-list operations, and apply binary search to answer-space problems.

In the lesson: The bisect module wraps exactly the loop invariant you just saw but handles edge cases correctly across all Python versions. The bisect-left function returns the leftmost insertion point for the target; for five it returns two, the insertion point for the value to keep the list sorted, which also happens to be the index of the existing five. Calling bisect-left with a value not in the list, such as four, still returns two, the position where four would go. Bisect-right returns one past the last occurrence, so for five it returns three. The insort function combines a bisect-left search with a list insertion, maintaining sorted order in a single call. The list after insort shows six placed between five and seven. For workloads with frequent insertion, insort on a plain list costs linear time per call because list insertion shifts elements; the advantage of bisect is log-n-time search, not constant-time insertion.

## Files

- [`starter/shell-the-bisect-module-in-the-shell.py`](starter/shell-the-bisect-module-in-the-shell.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l03/m04l03-04/starter`
2. Read `shell-the-bisect-module-in-the-shell.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   import bisect
   a = [1, 3, 5, 7, 9]
   bisect.bisect_left(a, 5)
   bisect.bisect_left(a, 4)
   bisect.bisect_right(a, 5)
   bisect.insort(a, 6)
   a
   ```
4. Run it: `python3 -i < shell-the-bisect-module-in-the-shell.py`.
5. Check it from the repository root: `./check m04l03-04`.

## Expected output

```text
2
2
3
[1, 3, 5, 6, 7, 9]
```

## How to check

`./check m04l03-04` copies `starter/` into a scratch directory and runs `python3 -i < shell-the-bisect-module-in-the-shell.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m04l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
