# Exercises — Collisions In Practice And Hash Flooding

Lesson `m02l04` · [Watch](https://learnsome.tech/courses/algorithms-course/watch?lesson=m02l04)

## Exercise 1: Measure collision rates and attack surfaces

1. Extend insert_chain to print the size of the longest chain after all inserts.
2. Find ten common English words that all land in the same slot under weak_slot with n=16.
3. Modify good_slot to use base 37 and compare its collision rate to base 31.

> **Hint**: For the anagram search, look for words that share the same letter sum modulo sixteen. Sort words by their weak_slot value and find the largest group. For collision rate, count how many of the inserted keys share a slot with at least one other key.


---

© LearnSome.tech · support@iwantto.learnsome.tech
