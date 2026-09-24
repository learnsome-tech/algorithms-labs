# Exercises — Minimum Spanning Trees: Kruskal And Prim

Lesson `m06l05` · [Watch](https://learnsome.tech/courses/algorithms-course/watch?lesson=m06l05)

## Exercise 1: Practice: extend the graph and verify the MST

1. Add a fifth vertex E connected to D and C, then run both Kruskal and Prim to compare totals.
2. Modify Kruskal to also print each edge it considers but rejects because it would form a cycle.
3. Print the parent array before and after find calls to observe path compression.

> **Hint**: Path compression flattens the parent tree on the recursive find call back, so a second call to find on any vertex in the same component returns immediately; printing the parent array before and after the first batch of finds shows the difference.


---

© LearnSome.tech · support@iwantto.learnsome.tech
