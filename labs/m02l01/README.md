# m02l01 · What A Hash Function Promises

Module 2: Hashing: Structure Behind Everything Fast · lesson 2.1 · Pro · [Open the lesson](https://learnsome.tech/learn/algorithms-course/m02l01)

**Goal:** You can explain the three core properties a hash function must have, implement a polynomial rolling hash, and reason about why Python randomises string hashing.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m02l01-02](m02l01-02/) | How Python hashes small integers | Graded |
| [m02l01-03](m02l01-03/) | Stable string digests with SHA two-fifty-six | Graded |
| [m02l01-04](m02l01-04/) | A rolling hash maps keys to buckets | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Explore hash distribution and stability

1. Modify poly_hash to use base 37 and compare the bucket distribution to base 31.
2. Write a function that returns True when two strings land in the same bucket.
3. Use hashlib.sha256 to show that the same word hashes identically across two calls.

> **Hint:** Call poly_hash on both strings with the same n and base, then compare the results. For the sha256 task, encode the strings to bytes and compare hexdigests directly.

## Check yourself

- What are the three core properties a hash function must have, and which fourth property do good implementations add?
- Why does Python return negative two when you call hash of negative one?
- What is PYTHONHASHSEED, and why does Python introduce randomness into string hashing by default?
- How does a polynomial rolling hash differ from simply summing the character codes of a string?
- Why is hashlib SHA two-fifty-six suitable for cross-process-stable string hashing when the built-in hash is not?

---

[Course README](../../README.md) · [Algorithms & Data Structures for Working Engineers on LearnSome.tech](https://learnsome.tech/courses/algorithms-course)
