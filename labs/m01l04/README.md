# m01l04 · Big O, Big Omega And Big Theta

Module 1: Complexity And Trade-offs · lesson 1.4 · Free · [Open the lesson](https://learnsome.tech/learn/algorithms-course/m01l04)

**Goal:** You can define big O, big Omega, and big Theta in words, verify an asymptotic claim empirically by checking the ratio of cost to n, and distinguish best, worst, and average case for linear search.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m01l04-02](m01l04-02/) | Checking an upper bound by watching the ratio | Graded |
| [m01l04-03](m01l04-03/) | Best, worst, and average case with linear search | Graded |
| [m01l04-04](m01l04-04/) | Watching the ratio with a simple function | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Apply the three bounds

1. Write a function that runs exactly n steps. Argue why it is Theta(n), not just O(n).
2. Write a linear search. What is its best-case Omega, worst-case O, and average-case Theta?
3. Confirm an O(n) claim by computing the ratio cost divided by n at five increasing sizes.

> **Hint:** For the ratio test: compute f(n) for n in [100, 1000, 10000, 100000] and print f(n) / n each time. A bounded ratio confirms O(n).

## Check yourself

- What is the difference between big O, big Omega, and big Theta? When do all three give the same growth rate?
- For linear search, what are the best-case, worst-case, and average-case comparison counts in a list of n elements?
- How does the ratio test work? What pattern in cost divided by n confirms an O(n) claim?
- Why is it common to use big O even when big Theta would be more precise?

---

[Course README](../../README.md) · [Algorithms & Data Structures for Working Engineers on LearnSome.tech](https://learnsome.tech/courses/algorithms-course)
