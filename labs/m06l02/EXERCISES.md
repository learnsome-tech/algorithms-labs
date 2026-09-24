# Exercises — Breadth-First Search And Shortest Paths By Hops

Lesson `m06l02` · [Watch](https://learnsome.tech/courses/algorithms-course/watch?lesson=m06l02)

## Exercise 1: Practice: extend the search and trace the queue

1. Add two new people to the graph and run BFS to find how many hops separate them from Alice.
2. Modify bfs_layers to also print the count of vertices in each layer.
3. Trace by hand which vertices are in the queue after each dequeue step starting from Alice.

> **Hint**: The queue always holds vertices at the current distance level or one level deeper; once you dequeue all vertices at level k, every remaining entry is at level k plus one.


---

© LearnSome.tech · support@iwantto.learnsome.tech
