# m05l02 · Binary Search Trees: Search, Insert And Delete

Module 5: Trees: Hierarchies, Search And Balance · lesson 5.2 · Pro · [Open the lesson](https://learnsome.tech/learn/algorithms-course/m05l02)

**Goal:** You can insert and search in a binary search tree, implement all three delete cases using the in-order successor, read a sorted in-order traversal as a correctness check, and explain why sorted insertion produces a degenerate tree of linear height.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m05l02-02](m05l02-02/) | BST insert and in-order verification | Graded |
| [m05l02-03](m05l02-03/) | Search and minimum in a BST | Graded |
| [m05l02-04](m05l02-04/) | BST delete: three cases | Graded |
| [m05l02-05](m05l02-05/) | Sorted insertion: the degenerate tree | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Exercises: extend the BST

1. Add a function that finds the BST maximum by walking right instead of left.
2. Extend delete to explicitly return the unchanged tree when the target value is not present.
3. Insert values one through fifty in sorted order and again shuffled, then print both heights.

> **Hint:** Maximum follows the same path as minimum but always turns right; shuffle with random.shuffle before inserting to observe the balanced case.

## Check yourself

- What is the BST property, and why does it guarantee that inorder traversal produces a sorted sequence?
- Describe the three cases that delete must handle and explain how the two-children case avoids breaking the BST invariant.
- Why does inserting keys in sorted ascending order produce the worst-case height for a plain BST?
- What is the time cost of search in a BST, and which input sequence achieves that worst case?
- Why is the in-order successor the correct replacement when deleting a node with two children?

---

[Course README](../../README.md) · [Algorithms & Data Structures for Working Engineers on LearnSome.tech](https://learnsome.tech/courses/algorithms-course)
