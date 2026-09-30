# m01l01 · Why Complexity Matters In Production

Module 1: Complexity And Trade-offs · lesson 1.1 · Free · [Open the lesson](https://learnsome.tech/learn/algorithms-course/m01l01)

**Goal:** You can explain why scanning a list grows linearly with input size while a dictionary lookup stays constant, measure both with the perf counter timer, and describe what input size n means in a complexity argument.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m01l01-02](m01l01-02/) | Scanning a list to find a user | Graded |
| [m01l01-03](m01l01-03/) | Measuring the gap with a timer | Graded |
| [m01l01-04](m01l01-04/) | Asking whether something is in a list or a dict | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Measure a lookup in your own code

1. Write a function that scans a list of integers for a target at the last position.
2. Convert it to use a dict. Compare both with time.perf_counter over a thousand repetitions.
3. Try doubling n and observe how each version's measured time changes.

> **Hint:** Build the list with list(range(n)) and the dict with {i: True for i in range(n)}. Put the target at n - 1 so the list always pays full cost.

## Check yourself

- Why does searching a list of ten thousand items for the last entry take more time than a dictionary lookup for the same entry?
- What does the variable n represent in a complexity argument, and why does it matter more than raw execution time?
- How would you use time.perf_counter to compare two implementations fairly, and why repeat the test many times?
- If doubling n doubles the running time of an algorithm, what does that tell you about its growth rate?
- What is the difference between a list scan and a hash table lookup in terms of how each finds a match?

---

[Course README](../../README.md) · [Algorithms & Data Structures for Working Engineers on LearnSome.tech](https://learnsome.tech/courses/algorithms-course)
