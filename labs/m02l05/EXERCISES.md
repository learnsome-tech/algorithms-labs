# Exercises — Bloom Filters: Membership Without The Data

Lesson `m02l05` · [Watch](https://learnsome.tech/courses/algorithms-course/watch?lesson=m02l05)

## Exercise 1: Tune and extend the Bloom filter

1. Add a method that estimates how many items have been inserted based on the bit count.
2. Find the value of k that minimises false positives for m=256 bits and n=30 items.
3. Implement a counting Bloom filter that increments a counter instead of setting a bit.

> **Hint**: For item count estimation, use the formula n = -m times the natural log of one minus fill rate over k, where fill rate is the fraction of set bits. For counting, replace each bit with a small integer and decrement on delete.


---

© LearnSome.tech · support@iwantto.learnsome.tech
