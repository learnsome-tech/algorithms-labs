# m06l03 · Depth-First Search, Cycles And Topological Order

Module 6: Graphs And Their Algorithms · lesson 6.3 · Pro · [Open the lesson](https://learnsome.tech/learn/algorithms-course/m06l03)

**Goal:** You can implement recursive DFS, detect a cycle in a directed graph using colour marking, and sort a dependency graph into valid execution order using Kahn's algorithm.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m06l03-02](m06l03-02/) | Recursive DFS: visit order through a directed graph | Graded |
| [m06l03-03](m06l03-03/) | Cycle detection with three-colour DFS marking | Graded |
| [m06l03-05](m06l03-05/) | Kahn's algorithm on a build-dependency graph | Graded |
| [m06l03-06](m06l03-06/) | Verifying the topological order | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Practice: add tasks and introduce a cycle

1. Add a new task depending on deploy to the graph and verify it appears last in the output.
2. Introduce a cycle by making compile depend on deploy and verify the output is incomplete.
3. Implement iterative DFS with an explicit stack and verify it visits the same vertices.

> **Hint:** When Kahn's algorithm encounters a cycle, some tasks never reach in-degree zero; compare the length of the output list with the total number of tasks to detect the missing entries.

## Check yourself

- What is a back edge in DFS, and why does finding one prove a directed cycle exists?
- Why does recursive DFS need a visited set, and what happens without one?
- What is a topological ordering, and why can it only exist for a DAG?
- How does Kahn's algorithm detect a cycle as a side effect?
- In the build dependency graph, why can link and test appear in either order in a valid topological sort?

---

[Course README](../../README.md) · [Algorithms & Data Structures for Working Engineers on LearnSome.tech](https://learnsome.tech/courses/algorithms-course)
