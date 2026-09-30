# m01l04-02 · Checking an upper bound by watching the ratio

**Lesson:** [Big O, Big Omega And Big Theta](https://learnsome.tech/learn/algorithms-course/m01l04) (lesson 1.4, module 1: Complexity And Trade-offs) · Free  
**Check:** Read along

## Goal

You can define big O, big Omega, and big Theta in words, verify an asymptotic claim empirically by checking the ratio of cost to n, and distinguish best, worst, and average case for linear search.

In the lesson: A linear work function counts exactly one operation per element. Divided by n, the ratio is always one: the cost per element is constant. That bounded ratio is exactly what big O of n means. The quadratic work function has a nested loop, so it counts n squared operations for each input size. The ratio of cost to n is not one but n itself, growing by a factor of ten each row. A function whose cost divided by n grows without bound cannot be called order n. Running both at three sizes makes the contrast unmistakable: the linear ratio stays flat while the ratio grows by a factor of one hundred between the smallest and largest input. Constant ratio equals bounded growth equals a valid O of n claim.

## Files

- [`starter/ratio_check.py`](starter/ratio_check.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/ratio_check.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–6: linear work function
   - Lines 7–12: nested loop
   - Lines 13–18: ratio grows by a factor

## How to check

**Read along.** The listing does not run cleanly in the lab sandbox (it relies on something the sandbox cannot provide), so the site shows it read-only.

There is nothing to check: `./check m01l04-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m01l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
