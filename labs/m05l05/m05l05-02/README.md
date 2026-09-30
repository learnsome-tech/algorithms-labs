# m05l05-02 · Array-backed min-heap with sift-up and sift-down

**Lesson:** [Heaps And Priority Queues](https://learnsome.tech/learn/algorithms-course/m05l05) (lesson 5.5, module 5: Trees: Hierarchies, Search And Balance) · Pro  
**Check:** Graded

## Goal

You can build an array-backed min-heap with sift-up and sift-down, use the heapq module for push, pop, heapify, and nlargest, implement heap sort, and model a priority queue as a task scheduler.

In the lesson: Building a heap from scratch requires two operations. Sift up moves a newly appended element toward the root as long as it is smaller than its parent: compare with the parent index, swap if needed, and repeat from the new position. Sift down moves a displaced element toward the leaves by repeatedly swapping it with its smallest child until neither child is smaller than it. The extraction procedure is the standard pattern: swap the root with the last element, pop the last position, then sift down from the new root. Insert five elements one by one, calling sift-up after each append. The resulting array is a valid min-heap: the smallest element, one, sits at index zero. Extract the minimum by moving the tail element to the front and sifting down. The min is one and the heap after extraction remains valid with four elements.

## Files

- [`starter/minheap.py`](starter/minheap.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l05/m05l05-02/starter`
2. Read `minheap.py` the way the lesson builds it:
   - Lines 1–5: sift up
   - Lines 6–13: sift down
   - Lines 14–21: insert five elements
3. Run it: `python3 minheap.py`.
4. Check it from the repository root: `./check m05l05-02`.

## Expected output

```text
min-heap array: [1, 3, 8, 5, 4]
extracted minimum: 1
heap after extraction: [3, 4, 8, 5]
```

## How to check

`./check m05l05-02` copies `starter/` into a scratch directory and runs `python3 minheap.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m05l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
