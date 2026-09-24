# Exercises — Counting And Radix Sort: Beating N Log N

Lesson `m04l02` · [Watch](https://learnsome.tech/courses/algorithms-course/watch?lesson=m04l02)

## Exercise 1: Adapt counting sort for string sorting

1. Extend counting sort to sort single lowercase letters using their alphabet position as the key.
2. Adapt radix sort for two-digit integers, two passes only, and verify with random.seed(42).
3. Time counting sort as k grows from ten to one million using time.perf_counter.

> **Hint**: For the letter sort, use ord(c) minus ord of a to get the integer key; the alphabet has twenty-six letters, so k equals twenty-six.


---

© LearnSome.tech · support@iwantto.learnsome.tech
