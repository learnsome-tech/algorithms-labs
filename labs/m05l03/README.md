# m05l03 · AVL Trees: Rotations That Keep The Guarantee

Module 5: Trees: Hierarchies, Search And Balance · lesson 5.3 · Pro · [Open the lesson](https://learnsome.tech/learn/algorithms-course/m05l03)

**Goal:** You can explain the AVL balance-factor invariant, implement single and double rotations, insert into an AVL tree with automatic rebalancing, and verify that sorted insertion keeps height logarithmic.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m05l03-02](m05l03-02/) | Left rotation: fixing a right-heavy chain | Graded |
| [m05l03-03](m05l03-03/) | AVL insert with single and double rotations | Graded |
| [m05l03-04](m05l03-04/) | Sorted insertion: AVL height stays logarithmic | Graded |
| [m05l03-06](m05l03-06/) | Logarithm bounds confirm the AVL heights | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Exercises: extend the AVL implementation

1. Implement right rotation and test with insertions three, two, one; verify root is two.
2. Count nodes with a non-zero balance factor to measure how often the tree leans to one side.
3. Extend AVL insert to reject duplicates and print a message when one is found.

> **Hint:** Right rotation is the mirror of left rotation: swap root and left child rather than root and right child, then fix heights bottom-up.

## Check yourself

- What is the balance factor of a node, and what values are permitted by the AVL invariant?
- Which imbalance case requires a double rotation, and what does the double rotation achieve that a single rotation cannot?
- Why does inserting keys in sorted order into an AVL tree keep height logarithmic while the same order collapses a plain BST to linear height?
- What is the height of an AVL tree that holds exactly one thousand and twenty-three nodes after sorted insertion?
- After a rotation, which nodes require a height update, and in what order should those updates be applied?

---

[Course README](../../README.md) · [Algorithms & Data Structures for Working Engineers on LearnSome.tech](https://learnsome.tech/courses/algorithms-course)
