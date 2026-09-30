# m06l02 · Breadth-First Search And Shortest Paths By Hops

Module 6: Graphs And Their Algorithms · lesson 6.2 · Pro · [Open the lesson](https://learnsome.tech/learn/algorithms-course/m06l02)

**Goal:** You can implement BFS with a deque to compute shortest hop distances and reconstruct paths, explain why BFS finds shortest paths in unweighted graphs, and use BFS to compute degrees of separation.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m06l02-02](m06l02-02/) | The deque as a FIFO queue | Graded |
| [m06l02-03](m06l02-03/) | BFS distance map on a social graph | Graded |
| [m06l02-04](m06l02-04/) | Path reconstruction using the parent map | Graded |
| [m06l02-05](m06l02-05/) | Level-order layers from the same BFS | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Practice: extend the search and trace the queue

1. Add two new people to the graph and run BFS to find how many hops separate them from Alice.
2. Modify bfs_layers to also print the count of vertices in each layer.
3. Trace by hand which vertices are in the queue after each dequeue step starting from Alice.

> **Hint:** The queue always holds vertices at the current distance level or one level deeper; once you dequeue all vertices at level k, every remaining entry is at level k plus one.

## Check yourself

- Why does BFS find shortest paths in an unweighted graph but not in a weighted one?
- What is the role of the deque in BFS, and what goes wrong if you use a stack instead?
- How do you reconstruct the shortest path after BFS finishes, given a parent map?
- What does layer two in a BFS layer listing tell you about those vertices?
- If a vertex is already in the distance map when BFS encounters it, why is it safe to skip?

---

[Course README](../../README.md) · [Algorithms & Data Structures for Working Engineers on LearnSome.tech](https://learnsome.tech/courses/algorithms-course)
