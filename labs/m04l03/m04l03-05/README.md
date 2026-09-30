# m04l03-05 · Searching an answer space with a monotone predicate

**Lesson:** [Binary Search And Its Invariant](https://learnsome.tech/learn/algorithms-course/m04l03) (lesson 4.3, module 4: Sorting And Searching) · Pro  
**Check:** Graded

## Goal

You can implement iterative binary search with a loop invariant, identify and fix common off-by-one errors, use the bisect module for sorted-list operations, and apply binary search to answer-space problems.

In the lesson: Any problem where the answer space is an integer range and there exists a threshold below which a predicate is false and at or above which it is true can be solved by bisection. The first-true function encodes this pattern with a different invariant: the predicate is false below lo and true at or above hi. When pred returns a result and the predicate turns true at mid, the answer is at most mid, so hi shrinks to mid. When pred returns false, the answer must be strictly above mid, so lo advances to mid plus one. The integer square root example searches for the smallest k whose square reaches or exceeds n; halving the search from zero to one hundred forty-four reaches twelve in eight steps. The pages question asks how many batches of two hundred fifty hold ten thousand records. Two answers appear without any loop over the answer space.

## Files

- [`starter/answer_space.py`](starter/answer_space.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l03/m04l03-05/starter`
2. Read `answer_space.py` the way the lesson builds it:
   - Lines 1–9: the predicate turns true
   - Lines 10–20: two answers appear
3. Run it: `python3 answer_space.py`.
4. Check it from the repository root: `./check m04l03-05`.

## Expected output

```text
integer sqrt of 144 is 12
minimum pages: 40
```

## How to check

`./check m04l03-05` copies `starter/` into a scratch directory and runs `python3 answer_space.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m04l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
