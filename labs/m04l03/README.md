# m04l03 · Binary Search And Its Invariant

Module 4: Sorting And Searching · lesson 4.3 · Pro · [Open the lesson](https://learnsome.tech/learn/algorithms-course/m04l03)

**Goal:** You can implement iterative binary search with a loop invariant, identify and fix common off-by-one errors, use the bisect module for sorted-list operations, and apply binary search to answer-space problems.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m04l03-02](m04l03-02/) | Iterative binary search with invariant comments | Graded |
| [m04l03-03](m04l03-03/) | Off-by-one: a one-character bug, a silent miss | Graded |
| [m04l03-04](m04l03-04/) | The bisect module in the Shell | Graded |
| [m04l03-05](m04l03-05/) | Searching an answer space with a monotone predicate | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Write and debug binary search variants

1. Implement binary search that returns the last occurrence of a target in a sorted list.
2. Use first_true to find the smallest k where k cubed is at least one million.
3. Add an iteration counter to binary search and print it for several different targets.

> **Hint:** For the last-occurrence search, when you find a match at mid you should not return immediately: keep searching rightward by updating lo rather than returning.

## Check yourself

- State the loop invariant for the correct binary search implementation in plain English.
- What does the off-by-one bug look like in code, and which targets does it fail to find?
- What is the difference between bisect-left and bisect-right when the target appears multiple times?
- How many iterations does binary search need to find an element in a sorted list of one billion entries?
- Describe a real system problem where you would apply first-true rather than searching a list directly.

---

[Course README](../../README.md) · [Algorithms & Data Structures for Working Engineers on LearnSome.tech](https://learnsome.tech/courses/algorithms-course)
