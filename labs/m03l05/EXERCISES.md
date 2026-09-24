# Exercises — Choosing The Right Sequence

Lesson `m03l05` · [Watch](https://learnsome.tech/courses/algorithms-course/watch?lesson=m03l05)

## Exercise 1: Sequence selection in practice

1. Design a rate limiter for sixty-second windows using a deque of timestamps; explain why.
2. Build a cache of the ten most recent unique values in insertion order, returned on request.
3. Write a verifier returning True when every pop retrieves the value most recently pushed.

> **Hint**: For the rate limiter, append new timestamps to the right and remove expired ones from the left; for unique ordered values, combine a set for membership testing with a deque for ordering.


---

© LearnSome.tech · support@iwantto.learnsome.tech
