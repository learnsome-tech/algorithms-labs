# m02l02 · Hash Tables: Chaining, Open Addressing And Load Factor

Module 2: Hashing: Structure Behind Everything Fast · lesson 2.2 · Pro · [Open the lesson](https://learnsome.tech/learn/algorithms-course/m02l02)

**Goal:** You can implement a chaining hash map and a linear-probing open-addressed table, explain what the load factor measures, and identify when and why a table must resize.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m02l02-02](m02l02-02/) | A chaining hash map stores pairs in bucket lists | Graded |
| [m02l02-03](m02l02-03/) | Tracking load factor and signalling a resize | Graded |
| [m02l02-04](m02l02-04/) | Linear probing fills the next free slot | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Extend the hash table implementations

1. Add a delete method to the ChainMap class that removes a key from its bucket list.
2. Modify lp_put to return the probe count and track the average across all inserts.
3. Insert keys that all map to slot zero and observe how the probe count grows with each.

> **Hint:** For chain deletion, walk the bucket list and pop the matching entry. For open addressing, mark the deleted slot with TOMB rather than EMPTY so that probing sequences past that position stay intact.

## Check yourself

- What does the load factor measure, and why does a high load factor hurt lookup performance in open addressing?
- Why must deletion in an open-addressed table leave a tombstone rather than marking the slot empty?
- In the chaining demo, why does the slot function use a cryptographic digest instead of Python's built-in hash?
- At what load factor did the demo signal a resize, and what would a real resize operation do to all existing entries?
- What is the main cache advantage of open addressing over chaining?

---

[Course README](../../README.md) · [Algorithms & Data Structures for Working Engineers on LearnSome.tech](https://learnsome.tech/courses/algorithms-course)
