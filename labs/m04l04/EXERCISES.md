# Exercises — Sorting In Real Systems: Stability, Keys And External Sort

Lesson `m04l04` · [Watch](https://learnsome.tech/courses/algorithms-course/watch?lesson=m04l04)

## Exercise 1: Sort real records and build a larger external merge

1. Sort log line dicts by timestamp then severity using operator.attrgetter or a lambda.
2. Split a list of one thousand integers into four sorted chunks and write each to a file.
3. Merge the four chunk files with heapq.merge and verify the result equals sorted of all chunks.

> **Hint**: For the external sort, generate data with random.seed(7), split into chunks of two hundred fifty, sort each chunk, and write one integer per line to files named chunk-zero through chunk-three.


---

© LearnSome.tech · support@iwantto.learnsome.tech
