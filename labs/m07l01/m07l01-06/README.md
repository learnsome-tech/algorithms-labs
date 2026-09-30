# m07l01-06 · Binary search: one branch, log n cost

**Lesson:** [Divide And Conquer And The Recurrence](https://learnsome.tech/learn/algorithms-course/m07l01) (lesson 7.1, module 7: Problem-Solving Techniques) · Pro  
**Check:** Graded

## Goal

You can apply the split-solve-combine pattern, explain why merge sort costs order n log n using its recurrence, implement a divide-and-conquer max-subarray and compare its operation count with brute force, and identify binary search as the one-branch case.

In the lesson: Binary search is divide and conquer with the combining step removed entirely. Compare the target with the middle element. If they match, done. If the target is smaller, the entire right half is eliminated. If larger, the left half goes. Either way, exactly one surviving half is passed to the next iteration.

Because the size halves on every step, the number of steps is bounded by log two of n. An array of sixty-four elements needs at most six comparisons: six halvings bring sixty-four down to one. The search for the value ninety-nine, which is not in the array, also terminates in six steps because the decision to discard a half does not depend on whether the target exists. Both searches finish in the same number of steps, confirming the logarithmic bound.

## Files

- [`starter/binsearch.py`](starter/binsearch.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m07l01/m07l01-06/starter`
2. Read `binsearch.py` the way the lesson builds it:
   - Lines 1–13: one surviving half
   - Lines 14–20: both searches finish
3. Run it: `python3 binsearch.py`.
4. Check it from the repository root: `./check m07l01-06`.

## Expected output

```text
found 64 at index 32 in 6 steps
search for 99 also took 6 steps
array has 64 elements
```

## How to check

`./check m07l01-06` copies `starter/` into a scratch directory and runs `python3 binsearch.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m07l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
