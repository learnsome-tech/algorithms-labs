# m02l05 · Bloom Filters: Membership Without The Data

Module 2: Hashing: Structure Behind Everything Fast · lesson 2.5 · Pro · [Open the lesson](https://learnsome.tech/learn/algorithms-course/m02l05)

**Goal:** You can implement a Bloom filter using k hash functions derived from SHA two-fifty-six, measure its false-positive rate on a fixed word list, and explain why Bloom filters guarantee zero false negatives.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m02l05-02](m02l05-02/) | A Bloom filter built on SHA two-fifty-six | Graded |
| [m02l05-03](m02l05-03/) | Measuring the false-positive rate on a fixed test set | Graded |
| [m02l05-04](m02l05-04/) | Larger bit arrays produce fewer false positives | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Tune and extend the Bloom filter

1. Add a method that estimates how many items have been inserted based on the bit count.
2. Find the value of k that minimises false positives for m=256 bits and n=30 items.
3. Implement a counting Bloom filter that increments a counter instead of setting a bit.

> **Hint:** For item count estimation, use the formula n = -m times the natural log of one minus fill rate over k, where fill rate is the fraction of set bits. For counting, replace each bit with a small integer and decrement on delete.

## Check yourself

- Why is a false negative impossible in a Bloom filter, and under what circumstance does a false positive occur?
- What happens to the false-positive rate when you increase the bit array size m while keeping n and k fixed?
- How does the prefix trick produce k independent hash positions from a single SHA two-fifty-six function?
- Why can you not delete an item from a basic Bloom filter, and what variant removes this restriction?
- In the three-size comparison, why did the five-hundred-and-twelve-bit filter show zero false positives for twenty items?

---

[Course README](../../README.md) · [Algorithms & Data Structures for Working Engineers on LearnSome.tech](https://learnsome.tech/courses/algorithms-course)
