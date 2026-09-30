# m07l04 · Dynamic Programming: Memoisation And Tabulation

Module 7: Problem-Solving Techniques · lesson 7.4 · Pro · [Open the lesson](https://learnsome.tech/learn/algorithms-course/m07l04)

**Goal:** You can explain overlapping subproblems and optimal substructure, apply memoisation with lru_cache to avoid redundant recursion, build a bottom-up tabulation table for the knapsack problem, and reconstruct a longest common subsequence from its DP table.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m07l04-02](m07l04-02/) | Fibonacci: naive recursion versus memoised recursion | Graded |
| [m07l04-03](m07l04-03/) | Knapsack tabulation: filling the DP table | Graded |
| [m07l04-04](m07l04-04/) | Longest common subsequence with reconstruction | Graded |
| [m07l04-05](m07l04-05/) | Edit distance: insertions, deletions and substitutions | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Practice: memoisation and tabulation

1. Trace the knapsack table backwards to recover which items are selected.
2. Write a memoised edit distance with lru_cache and verify it matches the tabulation version.
3. Count the number of distinct longest common subsequences for the two strings from this lesson.

> **Hint:** For knapsack reconstruction, start at dp[n][cap] and move up: if dp[i][w] differs from dp[i-1][w], item i was included and you subtract its weight from w before moving to row i minus one.

## Check yourself

- What are the two structural properties a problem must have for dynamic programming to apply, and which one explains why naive Fibonacci is exponential?
- How does functools.lru_cache implement memoisation, and what would you change to limit the cache size to one hundred entries?
- In the knapsack table, what does the value in row i and column w represent, and what two options does the recurrence consider?
- Describe how the LCS reconstruction works after the table is filled, and what decision is made at each step of the traceback.
- For edit distance, what do the three neighbours of an interior cell represent, and what does the diagonal neighbour represent when the two characters are equal?

---

[Course README](../../README.md) · [Algorithms & Data Structures for Working Engineers on LearnSome.tech](https://learnsome.tech/courses/algorithms-course)
