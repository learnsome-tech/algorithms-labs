# m04l03-03 · Off-by-one: a one-character bug, a silent miss

**Lesson:** [Binary Search And Its Invariant](https://learnsome.tech/learn/algorithms-course/m04l03) (lesson 4.3, module 4: Sorting And Searching) · Pro  
**Check:** Graded

## Goal

You can implement iterative binary search with a loop invariant, identify and fix common off-by-one errors, use the bisect module for sorted-list operations, and apply binary search to answer-space problems.

In the lesson: The buggy function uses strict less than in the while condition instead of at most. Watch what happens when lo and hi converge to the same index: the loop exits without checking that last position, returning negative one even though the target is right there. The value eighteen is the largest element in the even-number list, so the search interval collapses to exactly index nine without ever testing it. The miss appears in the first output line: negative one instead of nine. The interior element eight is found correctly by both versions because the midpoint calculation happens to land on it before convergence. One character change, from less than to at most, is all the fixed version needs. The invariant also changes with the bug: the strict less than condition implies half-open interval semantics requiring different update rules throughout the function, so the buggy version is inconsistent in two places at once.

## Files

- [`starter/obo.py`](starter/obo.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l03/m04l03-03/starter`
2. Read `obo.py` the way the lesson builds it:
   - Lines 1–8: strict less than in the while
   - Lines 9–20: the miss appears
3. Run it: `python3 obo.py`.
4. Check it from the repository root: `./check m04l03-03`.

## Expected output

```text
off-by-one on 18: -1
fixed on 18: 9
both on 8: 4 4
```

## How to check

`./check m04l03-03` copies `starter/` into a scratch directory and runs `python3 obo.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m04l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
