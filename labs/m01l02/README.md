# m01l02 · Recognising The Common Growth Rates

Module 1: Complexity And Trade-offs · lesson 1.2 · Free · [Open the lesson](https://learnsome.tech/learn/algorithms-course/m01l02)

**Goal:** You can name the five common growth rates, count operations for each pattern in code, and say which code structure produces which growth rate.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m01l02-02](m01l02-02/) | A growth table from counted operations | Graded |
| [m01l02-03](m01l02-03/) | Counting nested loop and halving operations | Graded |
| [m01l02-04](m01l02-04/) | Halving and the logarithm | Graded |
| [m01l02-06](m01l02-06/) | Counting work in a sort-based algorithm | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Classify the growth of code you write

1. Count operations in a for loop over range(n). How does the count grow when you double n?
2. Nest a second loop over range(n) inside the first. How fast do operations grow as n doubles?
3. Write a halving loop that counts iterations. Is the count close to log base two of n?

> **Hint:** Use a counter variable inside the loop body. Double n several times and record the counts to see the pattern.

## Check yourself

- What code structure produces quadratic complexity, and how would you recognise it by reading the code?
- Why does binary search run in logarithmic time, and what property of the algorithm causes this?
- A function has two nested loops each running from zero to n. What is its complexity, and how does the operation count change when n triples?
- Why is O(n log n) considered the best achievable complexity for comparison-based sorting?
- What growth rate does a single loop with a constant-time body have, regardless of the constant multiplier?

---

[Course README](../../README.md) · [Algorithms & Data Structures for Working Engineers on LearnSome.tech](https://learnsome.tech/courses/algorithms-course)
