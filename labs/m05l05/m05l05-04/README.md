# m05l05-04 · Heap sort

**Lesson:** [Heaps And Priority Queues](https://learnsome.tech/learn/algorithms-course/m05l05) (lesson 5.5, module 5: Trees: Hierarchies, Search And Balance) · Pro  
**Check:** Graded

## Goal

You can build an array-backed min-heap with sift-up and sift-down, use the heapq module for push, pop, heapify, and nlargest, implement heap sort, and model a priority queue as a task scheduler.

In the lesson: Heap sort follows naturally from the heap structure. Build a heap from the input list, then pop the minimum repeatedly; each pop returns the next smallest element because the heap always presents the minimum at the root. The implementation takes one line beyond heapify: a list comprehension that pops until the heap is empty. Heap sort costs order n for heapify and order n log n for the n pops, giving order n log n overall, the same asymptotic cost as merge sort. Unlike merge sort, heap sort does not need extra memory proportional to the input when implemented with a max-heap in place. The version here uses a copy for clarity. Apply it to a five-element list and confirm the output runs from smallest to largest.

## Files

- [`starter/heapsort.py`](starter/heapsort.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l05/m05l05-04/starter`
2. Read `heapsort.py` the way the lesson builds it:
   - Lines 1–6: heap sort
   - Lines 7–10: apply it to
3. Run it: `python3 heapsort.py`.
4. Check it from the repository root: `./check m05l05-04`.

## Expected output

```text
original: [64, 25, 12, 22, 11]
sorted: [11, 12, 22, 25, 64]
```

## How to check

`./check m05l05-04` copies `starter/` into a scratch directory and runs `python3 heapsort.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m05l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
