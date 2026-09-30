# m05l04 · B-Trees: The Structure Behind Every Database Index

Module 5: Trees: Hierarchies, Search And Balance · lesson 5.4 · Pro · [Open the lesson](https://learnsome.tech/learn/algorithms-course/m05l04)

**Goal:** You can explain the B-tree fan-out property, implement search and split-on-insert for a minimal B-tree, print node keys by level, and compute the maximum height for a million keys given a minimum degree.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m05l04-02](m05l04-02/) | Searching in a manually built B-tree | Graded |
| [m05l04-03](m05l04-03/) | B-tree insert with node splitting | Graded |
| [m05l04-04](m05l04-04/) | Height arithmetic for a million keys | Graded |
| [m05l04-05](m05l04-05/) | Printing B-tree keys level by level | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Exercises: extend the B-tree

1. Add a search function to btinsert.py that returns True if a key is present after insertion.
2. Modify by-level to also print the count of keys at each level and verify the tree is balanced.
3. Change minimum degree to three and rerun the insert test to observe how the tree changes shape.

> **Hint:** For degree three, each node holds at most five keys and splits on the sixth insertion into a node, producing a shallower and wider tree.

## Check yourself

- What does minimum degree t mean for the number of keys each B-tree node can hold, and how does t relate to fan-out?
- Explain why a B-tree with minimum degree five hundred twelve can hold one million keys in just two levels.
- What is the split operation in B-tree insertion, and at what point during an insert does it fire?
- Why do database B-plus trees store only keys in internal nodes rather than complete rows?

---

[Course README](../../README.md) · [Algorithms & Data Structures for Working Engineers on LearnSome.tech](https://learnsome.tech/courses/algorithms-course)
