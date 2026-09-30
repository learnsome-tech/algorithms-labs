# m04l01-02 · Insertion sort: shifting and counting

**Lesson:** [Comparison Sorts: Insertion, Merge And Quicksort](https://learnsome.tech/learn/algorithms-course/m04l01) (lesson 4.1, module 4: Sorting And Searching) · Pro  
**Check:** Graded

## Goal

You can implement insertion sort, merge sort, and quicksort with comparison counters, explain why no comparison sort beats order n log n, and demonstrate stability with tagged pairs.

In the lesson: Insertion sort wraps the comparison count in a mutable list so the nested inner function can reach back into the enclosing scope and update it. The outer loop picks each element starting from position one and saves it as key, then the inner while loop scans right to left through the sorted prefix, shifting every larger element one step rightward and incrementing the counter. The while loop stops when it encounters an element no larger than key or when it falls off the left end of the array. The displaced key value drops into the gap. Before calling the function you seed the random module with a fixed value so every run of this lesson sees the same ten-element list. The last four prints confirm the result: the original order, the sorted output, the exact comparison count, and the equality check against the built-in sort.

## Files

- [`starter/insertion_sort.py`](starter/insertion_sort.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l01/m04l01-02/starter`
2. Read `insertion_sort.py` the way the lesson builds it:
   - Lines 1–12: nested inner function
   - Lines 13–15: seed the random module
   - Lines 16–19: confirm the result
3. Run it: `python3 insertion_sort.py`.
4. Check it from the repository root: `./check m04l01-02`.

## Expected output

```text
before: [17, 72, 97, 8, 32, 15, 63, 97, 57, 60]
sorted: [8, 15, 17, 32, 57, 60, 63, 72, 97, 97]
comparisons: 19
verified: True
```

## How to check

`./check m04l01-02` copies `starter/` into a scratch directory and runs `python3 insertion_sort.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m04l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
