# Exercises — Depth-First Search, Cycles And Topological Order

Lesson `m06l03` · [Watch](https://learnsome.tech/courses/algorithms-course/watch?lesson=m06l03)

## Exercise 1: Practice: add tasks and introduce a cycle

1. Add a new task depending on deploy to the graph and verify it appears last in the output.
2. Introduce a cycle by making compile depend on deploy and verify the output is incomplete.
3. Implement iterative DFS with an explicit stack and verify it visits the same vertices.

> **Hint**: When Kahn's algorithm encounters a cycle, some tasks never reach in-degree zero; compare the length of the output list with the total number of tasks to detect the missing entries.


---

© LearnSome.tech · support@iwantto.learnsome.tech
