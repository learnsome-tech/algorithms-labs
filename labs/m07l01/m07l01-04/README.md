# m07l01-04 · Counting brute-force operations on max subarray

**Lesson:** [Divide And Conquer And The Recurrence](https://learnsome.tech/learn/algorithms-course/m07l01) (lesson 7.1, module 7: Problem-Solving Techniques) · Pro  
**Check:** Graded

## Goal

You can apply the split-solve-combine pattern, explain why merge sort costs order n log n using its recurrence, implement a divide-and-conquer max-subarray and compare its operation count with brute force, and identify binary search as the one-branch case.

In the lesson: The maximum subarray problem asks for the contiguous slice with the greatest sum. The brute force tries every pair of start and end indices, accumulating a running total and tracking the best seen so far. For an array of nine elements that is forty-five additions, one for each pair. In general, the number of pairs is n times n minus one over two, which is quadratic in n.

The array used here is a classic example: the best subarray runs from index three to six, summing to six. Printing the result confirms both the best sum and how many additions the two-pointer scan required. The quadratic growth becomes painful for large inputs: doubling the array size quadruples the work, which is why a smarter approach matters.

## Files

- [`starter/maxsub_brute.py`](starter/maxsub_brute.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m07l01/m07l01-04/starter`
2. Read `maxsub_brute.py` the way the lesson builds it:
   - Lines 1–11: brute force tries
   - Lines 12–17: printing the result
3. Run it: `python3 maxsub_brute.py`.
4. Check it from the repository root: `./check m07l01-04`.

## Expected output

```text
best sum: 6
operations: 45
brute force is quadratic in n
```

## How to check

`./check m07l01-04` copies `starter/` into a scratch directory and runs `python3 maxsub_brute.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m07l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
