# m04l03-02 · Iterative binary search with invariant comments

**Lesson:** [Binary Search And Its Invariant](https://learnsome.tech/learn/algorithms-course/m04l03) (lesson 4.3, module 4: Sorting And Searching) · Pro  
**Check:** Graded

## Goal

You can implement iterative binary search with a loop invariant, identify and fix common off-by-one errors, use the bisect module for sorted-list operations, and apply binary search to answer-space problems.

In the lesson: The invariant comment on the first line inside the function states the contract: if the target is present anywhere in the array, it must be in the subarray from lo to hi inclusive. Setting hi to the last index rather than the length ensures that lo and hi are always valid positions. The midpoint formula uses lo plus the floored half-distance rather than the simple average, which avoids integer overflow in languages where that matters and also makes the invariant reasoning cleaner. When the middle element is less than the target, lo advances to mid plus one; when it is greater, hi retreats to mid minus one. If lo exceeds hi the target is absent. The four searches execute and confirm that the function finds interior elements, reports missing values as negative one, and handles both the first and last positions correctly.

## Files

- [`starter/binsearch.py`](starter/binsearch.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l03/m04l03-02/starter`
2. Read `binsearch.py` the way the lesson builds it:
   - Lines 1–13: invariant comment
   - Lines 14–19: four searches execute
3. Run it: `python3 binsearch.py`.
4. Check it from the repository root: `./check m04l03-02`.

## Expected output

```text
find 7: 3
find 12: -1
find 1: 0
find 19: 9
```

## How to check

`./check m04l03-02` copies `starter/` into a scratch directory and runs `python3 binsearch.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m04l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
