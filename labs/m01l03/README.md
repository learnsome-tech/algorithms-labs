# m01l03 · Space, In-Place Work And The Call Stack

Module 1: Complexity And Trade-offs · lesson 1.3 · Free · [Open the lesson](https://learnsome.tech/learn/algorithms-course/m01l03)

**Goal:** You can distinguish auxiliary space from in-place algorithms, measure Python object sizes with sys.getsizeof, explain why deep recursion exhausts the call stack, and convert a recursive function to an iterative one.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m01l03-02](m01l03-02/) | Building a reversed copy and measuring list sizes | Graded |
| [m01l03-03](m01l03-03/) | Reversing in place, reusing the same memory | Graded |
| [m01l03-04](m01l03-04/) | Recursion and the call stack | Graded |
| [m01l03-05](m01l03-05/) | Converting recursion to iteration | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Analyse space and rewrite recursion

1. Write a function that returns a sorted copy of a list. What is its auxiliary space cost?
2. Sort a list in place with list.sort(). Use sys.getsizeof to verify the size is unchanged.
3. Convert a recursive Fibonacci function to iterative. How deep can the recursive version go?

> **Hint:** sys.getsizeof reports the container size, not the size of the items inside it. Compare sizes before and after to see whether extra space was allocated.

## Check yourself

- What is the difference between auxiliary space and an in-place algorithm, and which uses less extra memory?
- Why does Python raise RecursionError rather than silently overflowing the call stack?
- How would you convert a recursive sum to an iterative one, and what does that trade in terms of space cost?
- What does sys.getsizeof measure about a list, and why does it grow proportionally to the number of elements?

---

[Course README](../../README.md) · [Algorithms & Data Structures for Working Engineers on LearnSome.tech](https://learnsome.tech/courses/algorithms-course)
