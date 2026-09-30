# m04l01-04 · Quicksort: Lomuto partition in place

**Lesson:** [Comparison Sorts: Insertion, Merge And Quicksort](https://learnsome.tech/learn/algorithms-course/m04l01) (lesson 4.1, module 4: Sorting And Searching) · Pro  
**Check:** Graded

## Goal

You can implement insertion sort, merge sort, and quicksort with comparison counters, explain why no comparison sort beats order n log n, and demonstrate stability with tagged pairs.

In the lesson: The Lomuto partition scheme picks the last element of each subarray as the pivot. A sweep index crosses the subarray from left to right, and whenever it finds an element at most equal to the pivot, that element swaps into the growing low region. Every element compared against the pivot adds one to the counter. After the sweep, the pivot itself swaps into its final sorted position, and the function recurses on the Lomuto partition left and right parts. On this input the sort counts twenty one comparisons, fewer than merge sort. The output confirms the result is correct. Quicksort's comparison count varies with pivot choices: good pivots split the array near the middle, bad pivots create lopsided partitions and push performance toward the quadratic case.

## Files

- [`starter/quicksort.py`](starter/quicksort.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l01/m04l01-04/starter`
2. Read `quicksort.py` the way the lesson builds it:
   - Lines 1–14: Lomuto partition
   - Lines 15–21: twenty one comparisons
3. Run it: `python3 quicksort.py`.
4. Check it from the repository root: `./check m04l01-04`.

## Expected output

```text
before: [17, 72, 97, 8, 32, 15, 63, 97, 57, 60]
sorted: [8, 15, 17, 32, 57, 60, 63, 72, 97, 97]
comparisons: 21
verified: True
```

## How to check

`./check m04l01-04` copies `starter/` into a scratch directory and runs `python3 quicksort.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m04l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
