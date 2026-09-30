# m05l05-03 · The heapq module: heapify, push, pop, nlargest

**Lesson:** [Heaps And Priority Queues](https://learnsome.tech/learn/algorithms-course/m05l05) (lesson 5.5, module 5: Trees: Hierarchies, Search And Balance) · Pro  
**Check:** Graded

## Goal

You can build an array-backed min-heap with sift-up and sift-down, use the heapq module for push, pop, heapify, and nlargest, implement heap sort, and model a priority queue as a task scheduler.

In the lesson: The heapq module in the standard library wraps the array-heap algorithms you just built, and it is what you should use in production code. Heapify converts an arbitrary list into a valid min-heap in linear time by applying sift-down from the last non-leaf backward to the root, which is faster than inserting elements one by one. The resulting array for the six-element list starts with five at the root. Heappush adds a new element and restores the heap property with sift-up; adding fifty places it at the end and it stays there because fifty is larger than its parent. Heappop removes and returns the minimum, then repairs the heap. After popping five, the new minimum is seventeen. Nlargest returns the three largest values without sorting the whole collection, running in n log k time, which beats a full sort when k is small.

## Files

- [`starter/heapqops.py`](starter/heapqops.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l05/m05l05-03/starter`
2. Read `heapqops.py` the way the lesson builds it:
   - Lines 1–5: heapify converts
   - Lines 6–10: nlargest
3. Run it: `python3 heapqops.py`.
4. Check it from the repository root: `./check m05l05-03`.

## Expected output

```text
heapified: [5, 17, 31, 42, 63, 88]
after push: [5, 17, 31, 42, 63, 88, 50]
popped: 5
heap now: [17, 42, 31, 50, 63, 88]
three largest: [88, 63, 50]
```

## How to check

`./check m05l05-03` copies `starter/` into a scratch directory and runs `python3 heapqops.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m05l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
