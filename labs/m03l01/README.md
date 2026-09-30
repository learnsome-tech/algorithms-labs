# m03l01 · Arrays: Contiguous Memory And Constant-Time Access

Module 3: Sequences: Arrays, Lists, Stacks And Queues · lesson 3.1 · Pro · [Open the lesson](https://learnsome.tech/learn/algorithms-course/m03l01)

**Goal:** You can explain why array index access is constant time, measure the memory difference between a typed array and a list, predict the cost of front insertion versus appending, and describe why slicing produces a copy.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m03l01-02](m03l01-02/) | Measuring storage with array and list | Graded |
| [m03l01-03](m03l01-03/) | Verifying constant-time index access | Runs, not graded |
| [m03l01-04](m03l01-04/) | Counting the cost of front insertion | Graded |
| [m03l01-05](m03l01-05/) | Slices as independent copies | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Array experiments

1. Build an array.array('d') of ten floats and compare its getsizeof to a list of the same numbers.
2. Write slice_copy(lst, k) that returns the first k items as a copy; confirm it is a new object.
3. Time one thousand front inserts versus one thousand appends; print True if appending was faster.

> **Hint:** Use time.perf_counter before and after each timed loop, and import sys for the getsizeof comparison.

## Check yourself

- What arithmetic determines the address of an element in a contiguous array, and why does this make access constant time?
- Why does inserting at the front of a Python list cost more than appending to the back, and what is the cost in terms of growth rate?
- What is amortised constant time, and why does Python list append exhibit it despite occasional linear copies?
- Why does slicing a Python list return a copy rather than a view, and what bug does knowing this prevent?
- When would you choose array.array over a Python list for numeric data, and what do you give up by making that choice?

---

[Course README](../../README.md) · [Algorithms & Data Structures for Working Engineers on LearnSome.tech](https://learnsome.tech/courses/algorithms-course)
