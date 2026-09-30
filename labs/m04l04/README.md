# m04l04 · Sorting In Real Systems: Stability, Keys And External Sort

Module 4: Sorting And Searching · lesson 4.4 · Pro · [Open the lesson](https://learnsome.tech/learn/algorithms-course/m04l04)

**Goal:** You can sort with key functions and tuple keys, compose sorts by chaining stable passes, and implement a k-way external merge using heapq.merge over temporary files.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m04l04-02](m04l04-02/) | key=, reverse=, and operator.itemgetter | Graded |
| [m04l04-03](m04l04-03/) | Tuple keys for multi-column sorting | Graded |
| [m04l04-04](m04l04-04/) | Stability composition: sort secondary then primary | Graded |
| [m04l04-05](m04l04-05/) | K-way external merge with heapq.merge | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Sort real records and build a larger external merge

1. Sort log line dicts by timestamp then severity using operator.attrgetter or a lambda.
2. Split a list of one thousand integers into four sorted chunks and write each to a file.
3. Merge the four chunk files with heapq.merge and verify the result equals sorted of all chunks.

> **Hint:** For the external sort, generate data with random.seed(7), split into chunks of two hundred fifty, sort each chunk, and write one integer per line to files named chunk-zero through chunk-three.

## Check yourself

- What does the key argument to sorted do, and why is it more efficient than a comparison function?
- How do you sort by the second field descending and the first field ascending in one sorted call?
- What is stability composition and when would you use it instead of a tuple key?
- What does heapq.merge guarantee about memory usage when merging k sorted files?
- If Python's sort were not stable, what would go wrong in the two-pass stability composition example?

---

[Course README](../../README.md) · [Algorithms & Data Structures for Working Engineers on LearnSome.tech](https://learnsome.tech/courses/algorithms-course)
