# Exercises — Dijkstra: Shortest Paths With A Priority Queue

Lesson `m06l04` · [Watch](https://learnsome.tech/courses/algorithms-course/watch?lesson=m06l04)

## Exercise 1: Practice: extend the graph and trace the heap

1. Add a direct edge from A to E with weight six and verify whether the shortest path changes.
2. Extend dijkstra to also return a parent map, then print the full path from A to D.
3. Trace by hand what is in the heap after each pop, counting how many lazy-deletion skips occur.

> **Hint**: To build the parent map, record the source vertex whenever you update a distance; the number of skips equals the total number of heap pushes minus the number of vertices that end up in the final distance map.


---

© LearnSome.tech · support@iwantto.learnsome.tech
