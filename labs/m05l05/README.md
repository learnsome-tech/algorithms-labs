# m05l05 · Heaps And Priority Queues

Module 5: Trees: Hierarchies, Search And Balance · lesson 5.5 · Pro · [Open the lesson](https://learnsome.tech/learn/algorithms-course/m05l05)

**Goal:** You can build an array-backed min-heap with sift-up and sift-down, use the heapq module for push, pop, heapify, and nlargest, implement heap sort, and model a priority queue as a task scheduler.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m05l05-02](m05l05-02/) | Array-backed min-heap with sift-up and sift-down | Graded |
| [m05l05-03](m05l05-03/) | The heapq module: heapify, push, pop, nlargest | Graded |
| [m05l05-04](m05l05-04/) | Heap sort | Graded |
| [m05l05-05](m05l05-05/) | Task scheduler: priority queue in action | Graded |
| [m05l05-06](m05l05-06/) | Exploring heapq interactively | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Exercises: extend the heap

1. Build a max-heap by negating keys on push and on pop, then verify with five values.
2. Use heapq.merge to combine two sorted lists and verify the merged output is sorted.
3. Add priority updates to the scheduler using lazy deletion with a set of cancelled task ids.

> **Hint:** For lazy deletion, mark a task as cancelled in a set when its priority changes, push the new version, and skip cancelled entries during pop.

## Check yourself

- What is the parent index for a node at index seven in a zero-based heap array?
- Why does extracting the minimum from a min-heap require a sift-down rather than a sift-up after the root is removed?
- Heapify runs in linear time even though it applies sift-down to every non-leaf. Why is the total work linear rather than order n log n?
- Name two heapq operations that retrieve extreme values faster than sorting the full collection.
- How does a tuple with a priority number as its first element model a priority queue when using heapq?

---

[Course README](../../README.md) · [Algorithms & Data Structures for Working Engineers on LearnSome.tech](https://learnsome.tech/courses/algorithms-course)
