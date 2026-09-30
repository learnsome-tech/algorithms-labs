# m01l05 · Amortised Analysis: Why Append Is Cheap

Module 1: Complexity And Trade-offs · lesson 1.5 · Free · [Open the lesson](https://learnsome.tech/learn/algorithms-course/m01l05)

**Goal:** You can explain why appending to a dynamic array is amortised constant time by tracing the doubling strategy, compare it to fixed-increment growth, and state the credit argument for the amortised bound.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m01l05-02](m01l05-02/) | A dynamic array that counts its copies | Graded |
| [m01l05-03](m01l05-03/) | Fixed increment vs doubling: total copy cost | Graded |
| [m01l05-04](m01l05-04/) | Python list sizes in the shell | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Trace the dynamic array yourself

1. Trace the DynamicArray class for eight appends. List capacity at each append and total copies.
2. Change the growth rule to add half the current capacity. How does the total compare to doubling?
3. Count how many appends trigger a resize for two hundred and fifty-six items with doubling.

> **Hint:** The capacity sequence with doubling starting at one is: one, two, four, eight, and so on. A resize fires whenever length equals capacity before the append.

## Check yourself

- Why is appending to a Python list described as O(1) amortised, even though some individual appends cost O(n)?
- How many total element copies does a doubling dynamic array perform to hold n elements, in terms of n?
- What is the credit model argument that shows the amortised cost per append is constant?
- Why does fixed-increment growth lead to quadratic total copy cost while doubling leads to linear total cost?
- What does sys.getsizeof reveal about how Python pre-allocates space for a list?

---

[Course README](../../README.md) · [Algorithms & Data Structures for Working Engineers on LearnSome.tech](https://learnsome.tech/courses/algorithms-course)
