# m04l02 · Counting And Radix Sort: Beating N Log N

Module 4: Sorting And Searching · lesson 4.2 · Pro · [Open the lesson](https://learnsome.tech/learn/algorithms-course/m04l02)

**Goal:** You can implement counting sort and LSD radix sort, explain when each applies, and describe the memory cost that comes with bypassing element comparisons.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m04l02-02](m04l02-02/) | Counting sort: one pass to count, one to reconstruct | Graded |
| [m04l02-03](m04l02-03/) | Building the count array by hand | Graded |
| [m04l02-04](m04l02-04/) | LSD radix sort: sorting digit by digit | Graded |
| [m04l02-05](m04l02-05/) | When key range becomes the bottleneck | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Adapt counting sort for string sorting

1. Extend counting sort to sort single lowercase letters using their alphabet position as the key.
2. Adapt radix sort for two-digit integers, two passes only, and verify with random.seed(42).
3. Time counting sort as k grows from ten to one million using time.perf_counter.

> **Hint:** For the letter sort, use ord(c) minus ord of a to get the integer key; the alphabet has twenty-six letters, so k equals twenty-six.

## Check yourself

- What property of the keys allows counting sort to bypass the n log n lower bound?
- Why must each pass of LSD radix sort be stable for the algorithm to produce a correct result?
- If you have one million integers in the range zero to nine, how much memory does counting sort need?
- Give one situation where counting sort is clearly preferable and one where a comparison sort wins.
- What does LSD stand for and why do you process digits in that order rather than the reverse?

---

[Course README](../../README.md) · [Algorithms & Data Structures for Working Engineers on LearnSome.tech](https://learnsome.tech/courses/algorithms-course)
