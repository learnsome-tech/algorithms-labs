# m04l01 · Comparison Sorts: Insertion, Merge And Quicksort

Module 4: Sorting And Searching · lesson 4.1 · Pro · [Open the lesson](https://learnsome.tech/learn/algorithms-course/m04l01)

**Goal:** You can implement insertion sort, merge sort, and quicksort with comparison counters, explain why no comparison sort beats order n log n, and demonstrate stability with tagged pairs.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m04l01-02](m04l01-02/) | Insertion sort: shifting and counting | Graded |
| [m04l01-03](m04l01-03/) | Merge sort: divide, merge, and count | Graded |
| [m04l01-04](m04l01-04/) | Quicksort: Lomuto partition in place | Graded |
| [m04l01-05](m04l01-05/) | Comparison counts at three sizes | Graded |
| [m04l01-06](m04l01-06/) | Stability: keeping equal elements in order | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Explore and extend the three sorts

1. Count swaps in insertion sort and verify that swaps never exceed the comparison count.
2. Add a recursive call counter to merge sort and print both comparisons and call count.
3. Run quicksort on a sorted input and compare the comparison count to the random-input result.

> **Hint:** For the already-sorted test, try sizes ten, fifty, and one hundred with a list from range and compare to the counts you saw for random data.

## Check yourself

- Why can no comparison sort do better than order n log n in the worst case?
- In what situation is insertion sort faster than merge sort on the same input?
- Why does merge sort use more comparisons than insertion sort on this ten-element input?
- What does the Lomuto partition do with the pivot element after the sweep?
- What is stability, and why does the strict greater than condition in insertion sort guarantee it?

---

[Course README](../../README.md) · [Algorithms & Data Structures for Working Engineers on LearnSome.tech](https://learnsome.tech/courses/algorithms-course)
