# m05l05-06 · Exploring heapq interactively

**Lesson:** [Heaps And Priority Queues](https://learnsome.tech/learn/algorithms-course/m05l05) (lesson 5.5, module 5: Trees: Hierarchies, Search And Balance) · Pro  
**Check:** Graded

## Goal

You can build an array-backed min-heap with sift-up and sift-down, use the heapq module for push, pop, heapify, and nlargest, implement heap sort, and model a priority queue as a task scheduler.

In the lesson: The interpreter session confirms heapq behavior step by step. Start with a four-element list and call heapify in place. Inspecting the heapify result shows one at the front, the global minimum, with three to its left and seven to its right at the second level. Heapify rearranged the elements from their original order without sorting them completely: seven sits next to three, which is not sorted, but both are larger than one. Push two onto the heap, then ask for the minimum with pop. Pop returns one, still the global minimum despite the push of two. After the pop, the two smallest values remaining in the heap are two and three, which nsmallest confirms without requiring a full sort. The heap is a machine for extracting extremes efficiently, not for producing a fully sorted sequence.

## Files

- [`starter/shell-exploring-heapq-interactively.py`](starter/shell-exploring-heapq-interactively.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l05/m05l05-06/starter`
2. Read `shell-exploring-heapq-interactively.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   import heapq
   h = [4, 1, 7, 3]
   heapq.heapify(h)
   h
   heapq.heappush(h, 2)
   heapq.heappop(h)
   heapq.nsmallest(2, h)
   ```
4. Run it: `python3 -i < shell-exploring-heapq-interactively.py`.
5. Check it from the repository root: `./check m05l05-06`.

## Expected output

```text
[1, 3, 7, 4]
1
[2, 3]
```

## How to check

`./check m05l05-06` copies `starter/` into a scratch directory and runs `python3 -i < shell-exploring-heapq-interactively.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m05l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
