# m06l04 · Dijkstra: Shortest Paths With A Priority Queue

Module 6: Graphs And Their Algorithms · lesson 6.4 · Pro · [Open the lesson](https://learnsome.tech/learn/algorithms-course/m06l04)

**Goal:** You can implement Dijkstra with a min-heap and lazy deletion, compute shortest weighted paths and their costs, explain why the greedy step fails on negative edges, and state the complexity in plain terms.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m06l04-02](m06l04-02/) | The min-heap as a priority queue | Graded |
| [m06l04-03](m06l04-03/) | Dijkstra: distances on a weighted road graph | Graded |
| [m06l04-05](m06l04-05/) | Negative edge: where the greedy step goes wrong | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Practice: extend the graph and trace the heap

1. Add a direct edge from A to E with weight six and verify whether the shortest path changes.
2. Extend dijkstra to also return a parent map, then print the full path from A to D.
3. Trace by hand what is in the heap after each pop, counting how many lazy-deletion skips occur.

> **Hint:** To build the parent map, record the source vertex whenever you update a distance; the number of skips equals the total number of heap pushes minus the number of vertices that end up in the final distance map.

## Check yourself

- What does lazy deletion mean in Dijkstra, and why is it correct to skip the outdated entry?
- Why does Dijkstra fail to find shortest paths when an edge has a negative weight?
- What is the time complexity of Dijkstra with a binary min-heap, stated in words?
- In the road graph, why does the path to B cost three rather than four?
- What algorithm should you use instead of Dijkstra when some edge weights are negative?

---

[Course README](../../README.md) · [Algorithms & Data Structures for Working Engineers on LearnSome.tech](https://learnsome.tech/courses/algorithms-course)
