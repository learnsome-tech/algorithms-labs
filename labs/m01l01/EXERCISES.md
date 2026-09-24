# Exercises — Why Complexity Matters In Production

Lesson `m01l01` · [Watch](https://learnsome.tech/courses/algorithms-course/watch?lesson=m01l01)

## Exercise 1: Measure a lookup in your own code

1. Write a function that scans a list of integers for a target at the last position.
2. Convert it to use a dict. Compare both with time.perf_counter over a thousand repetitions.
3. Try doubling n and observe how each version's measured time changes.

> **Hint**: Build the list with list(range(n)) and the dict with {i: True for i in range(n)}. Put the target at n - 1 so the list always pays full cost.


---

© LearnSome.tech · support@iwantto.learnsome.tech
