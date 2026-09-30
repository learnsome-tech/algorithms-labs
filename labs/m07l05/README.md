# m07l05 · Recognising The Pattern

Module 7: Problem-Solving Techniques · lesson 7.5 · Pro · [Open the lesson](https://learnsome.tech/learn/algorithms-course/m07l05)

**Goal:** You can apply a four-question decision procedure to classify an unfamiliar problem as divide-and-conquer, greedy, backtracking, or dynamic programming, implement a rule-table classifier in Python, and verify that three approaches to the same problem agree on the answer.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m07l05-02](m07l05-02/) | A rule table that classifies problems | Graded |
| [m07l05-03](m07l05-03/) | Capstone: one problem solved three ways | Graded |
| [m07l05-04](m07l05-04/) | Verifying greedy equals optimal across a range | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Practice: classify and implement

1. Classify three: domino tiling, unweighted shortest path, and minimum palindrome cuts.
2. Check that greedy fails for coins one, three, four across amounts one through twelve.
3. Write a knapsack solver using both memoisation and tabulation and assert the answers agree.

> **Hint:** For domino tiling, ask whether you need all tilings or just a count: a count with overlapping subproblems is dynamic programming. For the coin counterexample, the mismatch should appear at amount six.

## Check yourself

- What are the four questions in the decision procedure, and in what order should you ask them?
- Why does the coin-change problem with US denominations admit the greedy approach, while the one-three-four system does not?
- Shortest-path in an unweighted graph belongs to which technique, and how would your answer change if the edges had positive weights?
- What is the difference between dynamic programming and divide and conquer in terms of problem structure, even though both use recursive decomposition?
- If a backtracking solution is too slow for the given input size, what are two ways to improve it before switching to a different technique entirely?

---

[Course README](../../README.md) · [Algorithms & Data Structures for Working Engineers on LearnSome.tech](https://learnsome.tech/courses/algorithms-course)
