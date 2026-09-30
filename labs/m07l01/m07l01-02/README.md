# m07l01-02 · Merge sort implements all three steps

**Lesson:** [Divide And Conquer And The Recurrence](https://learnsome.tech/learn/algorithms-course/m07l01) (lesson 7.1, module 7: Problem-Solving Techniques) · Pro  
**Check:** Graded

## Goal

You can apply the split-solve-combine pattern, explain why merge sort costs order n log n using its recurrence, implement a divide-and-conquer max-subarray and compare its operation count with brute force, and identify binary search as the one-branch case.

In the lesson: Merge sort divides the work by always splitting at the midpoint, then rebuilding in sorted order on the way back up. The merge helper takes two already-sorted lists and interleaves them: walk a pointer through each, always picking the smaller head, then append whatever remains from whichever side still has elements. That step costs exactly as many comparisons as the combined length of both halves.

Merge sort itself is remarkably compact. A list of length one is already sorted, so that is the base case. Otherwise split at the midpoint, recurse on each half, then merge the two sorted results. The recursion tree has log n levels, and each level does n total comparisons across all the merges at that depth. Calling it on a scrambled list shows the elements come back in ascending order.

## Files

- [`starter/mergesort.py`](starter/mergesort.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m07l01/m07l01-02/starter`
2. Read `mergesort.py` the way the lesson builds it:
   - Lines 1–11: merge helper
   - Lines 12–17: merge sort itself
   - Lines 18–20: calling it on
3. Run it: `python3 mergesort.py`.
4. Check it from the repository root: `./check m07l01-02`.

## Expected output

```text
[1, 2, 3, 5, 8, 9]
```

## How to check

`./check m07l01-02` copies `starter/` into a scratch directory and runs `python3 mergesort.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m07l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
