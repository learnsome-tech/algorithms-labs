# m02l04 · Collisions In Practice And Hash Flooding

Module 2: Hashing: Structure Behind Everything Fast · lesson 2.4 · Pro · [Open the lesson](https://learnsome.tech/learn/algorithms-course/m02l04)

**Goal:** You can demonstrate how a constant-return hash degrades lookup to linear time, show how anagram-based keys exploit a sum hash, and explain how per-process hash randomisation defends against flooding attacks.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m02l04-02](m02l04-02/) | Counting comparisons: constant hash versus polynomial hash | Graded |
| [m02l04-03](m02l04-03/) | Anagram keys all land in the same weak-hash bucket | Graded |
| [m02l04-04](m02l04-04/) | Integer hashes are stable across all runs | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Measure collision rates and attack surfaces

1. Extend insert_chain to print the size of the longest chain after all inserts.
2. Find ten common English words that all land in the same slot under weak_slot with n=16.
3. Modify good_slot to use base 37 and compare its collision rate to base 31.

> **Hint:** For the anagram search, look for words that share the same letter sum modulo sixteen. Sort words by their weak_slot value and find the largest group. For collision rate, count how many of the inserted keys share a slot with at least one other key.

## Check yourself

- How many total comparisons does inserting n keys into a constant-return hash table require, and what complexity class is that?
- Why do all anagrams of the same word always land in the same bucket under a sum-of-codes hash?
- What is PYTHONHASHSEED, and what is the difference between setting it to zero versus leaving it unset?
- Why does the polynomial rolling hash distribute anagram keys across more slots than the sum hash?
- Which Python types have their hashes randomised by PYTHONHASHSEED, and which are unaffected?

---

[Course README](../../README.md) · [Algorithms & Data Structures for Working Engineers on LearnSome.tech](https://learnsome.tech/courses/algorithms-course)
