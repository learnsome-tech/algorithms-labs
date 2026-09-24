# Exercises — Dynamic Programming: Memoisation And Tabulation

Lesson `m07l04` · [Watch](https://learnsome.tech/courses/algorithms-course/watch?lesson=m07l04)

## Exercise 1: Practice: memoisation and tabulation

1. Trace the knapsack table backwards to recover which items are selected.
2. Write a memoised edit distance with lru_cache and verify it matches the tabulation version.
3. Count the number of distinct longest common subsequences for the two strings from this lesson.

> **Hint**: For knapsack reconstruction, start at dp[n][cap] and move up: if dp[i][w] differs from dp[i-1][w], item i was included and you subtract its weight from w before moving to row i minus one.


---

© LearnSome.tech · support@iwantto.learnsome.tech
