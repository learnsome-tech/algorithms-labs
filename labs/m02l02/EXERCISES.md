# Exercises — Hash Tables: Chaining, Open Addressing And Load Factor

Lesson `m02l02` · [Watch](https://learnsome.tech/courses/algorithms-course/watch?lesson=m02l02)

## Exercise 1: Extend the hash table implementations

1. Add a delete method to the ChainMap class that removes a key from its bucket list.
2. Modify lp_put to return the probe count and track the average across all inserts.
3. Insert keys that all map to slot zero and observe how the probe count grows with each.

> **Hint**: For chain deletion, walk the bucket list and pop the matching entry. For open addressing, mark the deleted slot with TOMB rather than EMPTY so that probing sequences past that position stay intact.


---

© LearnSome.tech · support@iwantto.learnsome.tech
