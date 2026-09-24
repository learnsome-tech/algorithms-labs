# Exercises — Amortised Analysis: Why Append Is Cheap

Lesson `m01l05` · [Watch](https://learnsome.tech/courses/algorithms-course/watch?lesson=m01l05)

## Exercise 1: Trace the dynamic array yourself

1. Trace the DynamicArray class for eight appends. List capacity at each append and total copies.
2. Change the growth rule to add half the current capacity. How does the total compare to doubling?
3. Count how many appends trigger a resize for two hundred and fifty-six items with doubling.

> **Hint**: The capacity sequence with doubling starting at one is: one, two, four, eight, and so on. A resize fires whenever length equals capacity before the append.


---

© LearnSome.tech · support@iwantto.learnsome.tech
