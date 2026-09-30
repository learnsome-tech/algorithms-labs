# m05l01 · Binary Trees And Their Traversals

Module 5: Trees: Hierarchies, Search And Balance · lesson 5.1 · Pro · [Open the lesson](https://learnsome.tech/learn/algorithms-course/m05l01)

**Goal:** You can build a binary tree with a node class, write recursive in-order, pre-order, and post-order traversals, implement level-order traversal with a deque, and compute height and node count.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m05l01-02](m05l01-02/) | A Node class and a seven-node tree | Graded |
| [m05l01-03](m05l01-03/) | In-order, pre-order and post-order traversals | Graded |
| [m05l01-04](m05l01-04/) | Level-order traversal with a deque | Graded |
| [m05l01-05](m05l01-05/) | Height and node count | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Exercises: extend the tree and the traversals

1. Add two children under node twelve and verify that height and count both update correctly.
2. Write a reverse inorder that visits right before left and prints values largest to smallest.
3. Modify level-order to print each level on its own line instead of a single flat list.

> **Hint:** For level-order by levels, track depth alongside each node in the queue or count how many nodes are in the current level before enqueueing children.

## Check yourself

- What does inorder traversal produce when applied to a binary search tree, and why does that property not hold for an arbitrary binary tree?
- Why does level-order traversal use a queue rather than a stack, and what would happen if you replaced the queue with a stack?
- Preorder traversal visits the root before its children. Name one task where this order is the natural choice.
- What is the time cost of computing height, and what determines the maximum stack depth during the recursion?
- A complete binary tree of height four holds exactly how many nodes, and how does that compare with seven nodes at height three?

---

[Course README](../../README.md) · [Algorithms & Data Structures for Working Engineers on LearnSome.tech](https://learnsome.tech/courses/algorithms-course)
