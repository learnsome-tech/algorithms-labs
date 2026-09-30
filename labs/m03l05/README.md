# m03l05 · Choosing The Right Sequence

Module 3: Sequences: Arrays, Lists, Stacks And Queues · lesson 3.5 · Pro · [Open the lesson](https://learnsome.tech/learn/algorithms-course/m03l05)

**Goal:** You can apply five diagnostic questions to select the right sequence structure, read a performance benchmark comparing list and deque, and explain why list and deque perform similarly for a pure stack workload.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m03l05-02](m03l05-02/) | Decision table for common scenarios | Graded |
| [m03l05-03](m03l05-03/) | Benchmark: front insertion and index access | Graded |
| [m03l05-05](m03l05-05/) | When list and deque perform alike | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Sequence selection in practice

1. Design a rate limiter for sixty-second windows using a deque of timestamps; explain why.
2. Build a cache of the ten most recent unique values in insertion order, returned on request.
3. Write a verifier returning True when every pop retrieves the value most recently pushed.

> **Hint:** For the rate limiter, append new timestamps to the right and remove expired ones from the left; for unique ordered values, combine a set for membership testing with a deque for ordering.

## Check yourself

- What are the five questions for choosing a sequence, and which one separates a list from a deque?
- Why does a deque outperform a list for front insertion, and why does a list outperform a deque for middle index access?
- Which scenario in the decision table is not actually a sequence problem, and what structure does it map to instead?
- Why do list and deque perform similarly for a pure stack workload where only one end is used?
- When should you choose a ring buffer over a maxlen deque, and what do you gain by the extra complexity?

---

[Course README](../../README.md) · [Algorithms & Data Structures for Working Engineers on LearnSome.tech](https://learnsome.tech/courses/algorithms-course)
