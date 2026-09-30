# m03l03 · Stacks And Queues: Last In Or First In

Module 3: Sequences: Arrays, Lists, Stacks And Queues · lesson 3.3 · Pro · [Open the lesson](https://learnsome.tech/learn/algorithms-course/m03l03)

**Goal:** You can implement a stack using a Python list and a queue using a deque, explain the ordering discipline of each, use a stack to check balanced brackets, and measure why list.pop(0) is a poor queue implementation.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m03l03-02](m03l03-02/) | Stack operations on a Python list | Graded |
| [m03l03-03](m03l03-03/) | Balanced brackets with a stack | Graded |
| [m03l03-05](m03l03-05/) | Simulating a print queue with deque | Graded |
| [m03l03-06](m03l03-06/) | Measuring pop-zero against popleft | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Stack and queue problems

1. Write eval_stack(ops) that processes 'push N' and 'pop' strings and returns the final stack.
2. Upgrade the brackets checker to report the position of the first mismatched bracket.
3. Build a bounded task queue with maxlen five; submitting when full silently drops the oldest job.

> **Hint:** For the position reporter, store the source index alongside each opener when you push onto the stack, so you can retrieve it when a mismatch is detected.

## Check yourself

- What ordering discipline does a stack enforce, and which method on a Python list serves as the push operation?
- Why is list.pop(0) a poor implementation of a queue dequeue operation, and what should you use instead?
- How does the balanced-brackets checker use the stack to detect a mismatch between an opener and its closer?
- What does the benchmark reveal about the trade-off between list and deque for front insertion versus middle-index access?
- Name two workloads that call for a stack and two that call for a queue, and explain the ordering reason in each case.

---

[Course README](../../README.md) · [Algorithms & Data Structures for Working Engineers on LearnSome.tech](https://learnsome.tech/courses/algorithms-course)
