# Exercises — What A Hash Function Promises

Lesson `m02l01` · [Watch](https://learnsome.tech/courses/algorithms-course/watch?lesson=m02l01)

## Exercise 1: Explore hash distribution and stability

1. Modify poly_hash to use base 37 and compare the bucket distribution to base 31.
2. Write a function that returns True when two strings land in the same bucket.
3. Use hashlib.sha256 to show that the same word hashes identically across two calls.

> **Hint**: Call poly_hash on both strings with the same n and base, then compare the results. For the sha256 task, encode the strings to bytes and compare hexdigests directly.


---

© LearnSome.tech · support@iwantto.learnsome.tech
