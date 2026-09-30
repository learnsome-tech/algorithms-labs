# m07l01 · Divide And Conquer And The Recurrence

Module 7: Problem-Solving Techniques · lesson 7.1 · Pro · [Open the lesson](https://learnsome.tech/learn/algorithms-course/m07l01)

**Goal:** You can apply the split-solve-combine pattern, explain why merge sort costs order n log n using its recurrence, implement a divide-and-conquer max-subarray and compare its operation count with brute force, and identify binary search as the one-branch case.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m07l01-02](m07l01-02/) | Merge sort implements all three steps | Graded |
| [m07l01-04](m07l01-04/) | Counting brute-force operations on max subarray | Graded |
| [m07l01-05](m07l01-05/) | Divide and conquer cuts the work to n log n | Graded |
| [m07l01-06](m07l01-06/) | Binary search: one branch, log n cost | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Practice: recurrence and implementation

1. Find both min and max by divide and conquer: split in half, recurse, then combine results.
2. Write the recurrence T(n) for your implementation and argue in words why it resolves to O(n).
3. Add a counter and confirm your function uses fewer than n comparisons for n equal to sixteen.

> **Hint:** At the base case of two elements, one comparison suffices to find both the min and the max. When you merge two pairs of results, two comparisons are enough: compare the two minimums and the two maximums.

## Check yourself

- What are the three steps of divide and conquer, and which step is responsible for the n term in the merge sort recurrence?
- Why does binary search cost order log n rather than order n log n even though it also splits the input in half?
- The max-subarray divide-and-conquer function checks three candidates at each recursive level. What are they, and which one requires a helper function?
- If a divide-and-conquer algorithm makes three recursive calls on thirds and its combine step costs linear time, what does its recurrence look like?
- How many comparisons does binary search need on a sorted array of one thousand and twenty-four elements, and why?

---

[Course README](../../README.md) · [Algorithms & Data Structures for Working Engineers on LearnSome.tech](https://learnsome.tech/courses/algorithms-course)
