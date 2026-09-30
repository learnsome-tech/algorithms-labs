# m06l05 · Minimum Spanning Trees: Kruskal And Prim

Module 6: Graphs And Their Algorithms · lesson 6.5 · Pro · [Open the lesson](https://learnsome.tech/learn/algorithms-course/m06l05)

**Goal:** You can implement union-find with path compression and union by rank, run Kruskal's algorithm to build a minimum spanning tree edge by edge, and run Prim's algorithm from a starting vertex using a heap.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m06l05-02](m06l05-02/) | Union-find: path compression and union by rank | Graded |
| [m06l05-03](m06l05-03/) | Kruskal's algorithm: growing the MST edge by edge | Graded |
| [m06l05-04](m06l05-04/) | Prim's algorithm: growing from a root vertex | Graded |
| [m06l05-05](m06l05-05/) | Inspecting the MST edge list | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Practice: extend the graph and verify the MST

1. Add a fifth vertex E connected to D and C, then run both Kruskal and Prim to compare totals.
2. Modify Kruskal to also print each edge it considers but rejects because it would form a cycle.
3. Print the parent array before and after find calls to observe path compression.

> **Hint:** Path compression flattens the parent tree on the recursive find call back, so a second call to find on any vertex in the same component returns immediately; printing the parent array before and after the first batch of finds shows the difference.

## Check yourself

- What is a spanning tree, and how many edges does one have for a graph with V vertices?
- What does path compression do in union-find, and why does it not change the correctness of the result?
- In what order does Kruskal process edges, and how does it decide whether to include an edge?
- Why do Kruskal and Prim always produce spanning trees of the same total weight, even if they choose different edges?
- What is the cut property, and how does it justify the greedy step in both algorithms?

---

[Course README](../../README.md) · [Algorithms & Data Structures for Working Engineers on LearnSome.tech](https://learnsome.tech/courses/algorithms-course)
