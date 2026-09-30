# m04l01-03 · Merge sort: divide, merge, and count

**Lesson:** [Comparison Sorts: Insertion, Merge And Quicksort](https://learnsome.tech/learn/algorithms-course/m04l01) (lesson 4.1, module 4: Sorting And Searching) · Pro  
**Check:** Graded

## Goal

You can implement insertion sort, merge sort, and quicksort with comparison counters, explain why no comparison sort beats order n log n, and demonstrate stability with tagged pairs.

In the lesson: Merge sort uses two nested functions. The merge helper takes two already-sorted lists and combines them by advancing two index pointers, each time picking the smaller front element and counting one comparison. When one list is exhausted, the tail of the other copies in without any further comparison. The sort function splits its input at the midpoint, recurses on each half, then hands both results to merge. On the same ten-element input, merge sort uses twenty-five comparisons, more than insertion sort managed here. That is not unusual at small sizes: the merge step always pays for comparisons that scan across both halves, whereas insertion sort only pays for moves. The seed value one ensures the same input as the previous segment, and the sorted result appears matching the built-in sort.

## Files

- [`starter/merge_sort.py`](starter/merge_sort.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l01/m04l01-03/starter`
2. Read `merge_sort.py` the way the lesson builds it:
   - Lines 1–15: merge helper
   - Lines 16–18: the seed value
   - Lines 19–22: the sorted result appears
3. Run it: `python3 merge_sort.py`.
4. Check it from the repository root: `./check m04l01-03`.

## Expected output

```text
before: [17, 72, 97, 8, 32, 15, 63, 97, 57, 60]
sorted: [8, 15, 17, 32, 57, 60, 63, 72, 97, 97]
comparisons: 25
verified: True
```

## How to check

`./check m04l01-03` copies `starter/` into a scratch directory and runs `python3 merge_sort.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m04l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
