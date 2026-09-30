# m07l01-05 · Divide and conquer cuts the work to n log n

**Lesson:** [Divide And Conquer And The Recurrence](https://learnsome.tech/learn/algorithms-course/m07l01) (lesson 7.1, module 7: Problem-Solving Techniques) · Pro  
**Check:** Graded

## Goal

You can apply the split-solve-combine pattern, explain why merge sort costs order n log n using its recurrence, implement a divide-and-conquer max-subarray and compare its operation count with brute force, and identify binary search as the one-branch case.

In the lesson: The divide-and-conquer version identifies three candidates at each recursive level. The best subarray either lies entirely in the left half, entirely in the right half, or it crosses the midpoint. The crossing subarray helper sweeps inward from the midpoint in both directions, tracking the running maximum on each side, and returns their sum.

The main function handles the base case of a single element and then passes the three candidates to the built-in max. Two of the three come from recursive calls; the third is the crossing helper. Running this on the same nine-element array gives the same answer as the brute force.

The cost recurrence is the standard divide-and-conquer shape: two halves plus linear work for the crossing scan. Three candidates emerge from that structure. Running it confirms the answer matches while the work grows as order n log n rather than quadratic.

## Files

- [`starter/maxsub_dc.py`](starter/maxsub_dc.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m07l01/m07l01-05/starter`
2. Read `maxsub_dc.py` the way the lesson builds it:
   - Lines 1–9: crossing subarray
   - Lines 10–17: three candidates
   - Lines 18–21: running it confirms
3. Run it: `python3 maxsub_dc.py`.
4. Check it from the repository root: `./check m07l01-05`.

## Expected output

```text
best sum: 6
divide and conquer is order n log n
```

## How to check

`./check m07l01-05` copies `starter/` into a scratch directory and runs `python3 maxsub_dc.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m07l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
