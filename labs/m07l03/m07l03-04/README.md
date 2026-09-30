# m07l03-04 · Generating all permutations with a recursive generator

**Lesson:** [Backtracking: Search With Pruning](https://learnsome.tech/learn/algorithms-course/m07l03) (lesson 7.3, module 7: Problem-Solving Techniques) · Pro  
**Check:** Graded

## Goal

You can implement backtracking with pruning, count solutions for N-queens and compare solution counts across board sizes, measure how much pruning reduces the nodes visited versus exhaustive search, and generate permutations with a recursive generator.

In the lesson: A permutation generator is backtracking without pruning, because every arrangement is a valid solution. The function is a generator that yields one complete permutation per leaf. The base case of a single item yields that item as a one-element tuple.

For longer lists, put each element as the first position in turn, then recursively generate all permutations of the remaining elements and prepend the chosen first element to each. The recursive structure ensures every ordering is produced exactly once.

Four items produce twenty-four permutations, which is four factorial. The first four of those are shown, all starting with one: the second position takes each remaining value in turn before the first position advances to two. Collecting four of them and printing confirms the ordering and that the total count is correct.

## Files

- [`starter/permutations.py`](starter/permutations.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m07l03/m07l03-04/starter`
2. Read `permutations.py` the way the lesson builds it:
   - Lines 1: generator that yields
   - Lines 2–8: each element as the first
   - Lines 9–13: collecting four of them
3. Run it: `python3 permutations.py`.
4. Check it from the repository root: `./check m07l03-04`.

## Expected output

```text
count: 24
  (1, 2, 3, 4)
  (1, 2, 4, 3)
  (1, 3, 2, 4)
  (1, 3, 4, 2)
```

## How to check

`./check m07l03-04` copies `starter/` into a scratch directory and runs `python3 permutations.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m07l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
