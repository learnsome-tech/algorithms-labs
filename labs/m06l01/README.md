# m06l01 · Representing A Graph: Matrix Or Adjacency List

Module 6: Graphs And Their Algorithms · lesson 6.1 · Pro · [Open the lesson](https://learnsome.tech/learn/algorithms-course/m06l01)

**Goal:** You can represent a graph as either an adjacency list or a two-dimensional matrix, state the memory cost of each, explain when to prefer one over the other, and encode directed and weighted edges.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m06l01-02](m06l01-02/) | Adjacency list: a dictionary of neighbour lists | Graded |
| [m06l01-03](m06l01-03/) | Adjacency matrix: a two-dimensional grid | Graded |
| [m06l01-04](m06l01-04/) | Space: sparse versus dense graphs | Graded |
| [m06l01-06](m06l01-06/) | Weighted directed graph with tuple adjacency lists | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Practice: extend and query the graph

1. Add vertex F connected to C and E in the adjacency list, then reprint the edge count.
2. Build the same five-vertex undirected graph as a matrix and confirm A's neighbours match.
3. Add integer weights to the undirected graph by changing each plain name to a tuple.

> **Hint:** For the undirected matrix, set both matrix[i][j] and matrix[j][i] to the weight so the edge is reachable from both directions.

## Check yourself

- What is the memory cost of an adjacency list for a graph with V vertices and E edges?
- Why does each undirected edge appear twice in an adjacency list?
- When would you choose an adjacency matrix over an adjacency list?
- How do you store a weighted directed edge in an adjacency list?
- If V equals one thousand and E equals three thousand, how many cells does the matrix need compared with the list?

---

[Course README](../../README.md) · [Algorithms & Data Structures for Working Engineers on LearnSome.tech](https://learnsome.tech/courses/algorithms-course)
