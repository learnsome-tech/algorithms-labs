# m06l04-02 · The min-heap as a priority queue

**Lesson:** [Dijkstra: Shortest Paths With A Priority Queue](https://learnsome.tech/learn/algorithms-course/m06l04) (lesson 6.4, module 6: Graphs And Their Algorithms) · Pro  
**Check:** Graded

## Goal

You can implement Dijkstra with a min-heap and lazy deletion, compute shortest weighted paths and their costs, explain why the greedy step fails on negative edges, and state the complexity in plain terms.

In the lesson: Python's heapq module maintains a list as a min-heap. After pushing three pairs, the smallest cost first comes out regardless of insertion order: the pair with cost one is popped before the pair with cost three. Dijkstra uses exactly this property: each push adds a candidate path to a vertex, and each pop retrieves the cheapest one. Tuples are compared element by element, so the cost comes first in the pair and the vertex name second. If two paths have the same cost, the vertex name breaks the tie, which is acceptable because both would produce a valid shortest path. Pushing the same vertex more than once is the lazy-deletion pattern: one entry will be popped and processed, and the others will be skipped when they emerge because their cost will exceed the recorded best.

## Files

- [`starter/shell-the-min-heap-as-a-priority-queue.py`](starter/shell-the-min-heap-as-a-priority-queue.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l04/m06l04-02/starter`
2. Read `shell-the-min-heap-as-a-priority-queue.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   import heapq
   h = []
   heapq.heappush(h, (3, 'B'))
   heapq.heappush(h, (1, 'A'))
   heapq.heappush(h, (4, 'C'))
   heapq.heappop(h)
   heapq.heappop(h)
   ```
4. Run it: `python3 -i < shell-the-min-heap-as-a-priority-queue.py`.
5. Check it from the repository root: `./check m06l04-02`.

## Expected output

```text
(1, 'A')
(3, 'B')
```

## How to check

`./check m06l04-02` copies `starter/` into a scratch directory and runs `python3 -i < shell-the-min-heap-as-a-priority-queue.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m06l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
