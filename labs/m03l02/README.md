# m03l02 · Linked Lists: Nodes, Pointers And Sentinels

Module 3: Sequences: Arrays, Lists, Stacks And Queues · lesson 3.2 · Pro · [Open the lesson](https://learnsome.tech/learn/algorithms-course/m03l02)

**Goal:** You can implement a singly linked list with push-front, append, delete, and find; explain why a sentinel head eliminates edge cases; and identify workloads where a linked list outperforms a Python list.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m03l02-02](m03l02-02/) | Building a singly linked list | Graded |
| [m03l02-03](m03l02-03/) | Deletion and linear search | Graded |
| [m03l02-05](m03l02-05/) | Sentinel head removes special cases | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Linked list surgery

1. Add push_after(target, val) to SLL: insert a new node after the node holding the value target.
2. Write reverse(head) to reverse a linked list in place by relinking nodes; return the new head.
3. Add a length counter to the sentinel list that updates on every insertion or deletion.

> **Hint:** For reversal, maintain three pointers: previous set to None, current set to head, and a saved-next variable updated at the start of each iteration.

## Check yourself

- What makes lookup by index linear in a linked list but constant in a contiguous array?
- What is a sentinel node, what value does it hold, and what category of edge cases does it eliminate?
- What is the time cost of deleting a node when you already hold a pointer to its predecessor?
- In the standalone delete function, what does the function return when the target is the head node?
- Name a real workload where a linked list deletion is faster than a Python list deletion, and explain why.

---

[Course README](../../README.md) · [Algorithms & Data Structures for Working Engineers on LearnSome.tech](https://learnsome.tech/courses/algorithms-course)
