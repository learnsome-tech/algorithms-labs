# m04l05-03 · Range queries: where sorted order wins

**Lesson:** [Searching With Hashes Versus Trees](https://learnsome.tech/learn/algorithms-course/m04l05) (lesson 4.5, module 4: Sorting And Searching) · Pro  
**Check:** Graded

## Goal

You can choose between a set, a sorted list with bisect, and a linear scan for membership and range queries, and explain when sorted order provides capabilities that hashing cannot.

In the lesson: The data list holds every third integer from zero to nine hundred ninety-nine, giving over three hundred elements. The sorted versus set range query comparison asks for all values between one hundred and one hundred twenty-five inclusive. The sorted list version uses bisect-left to find the insertion point for the lower bound and bisect-right to find the position after the upper bound, then slices out exactly those elements in order log n plus k steps. The set version must scan every element in the set and filter the ones in range, which costs order n regardless of how small the result is. Both produce the same eight multiples of three in that range, but the set version gets slower as the set grows while the sorted list version depends only on log n for finding boundaries and k for collecting results. A hash set cannot locate a boundary position at all.

## Files

- [`starter/range_query.py`](starter/range_query.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l05/m04l05-03/starter`
2. Read `range_query.py` the way the lesson builds it:
   - Lines 1–12: sorted versus set range query
   - Lines 13–15: both produce the same
3. Run it: `python3 range_query.py`.
4. Check it from the repository root: `./check m04l05-03`.

## Expected output

```text
sorted list range [100, 125]: [102, 105, 108, 111, 114, 117, 120, 123]
set range [100, 125]:         [102, 105, 108, 111, 114, 117, 120, 123]
```

## How to check

`./check m04l05-03` copies `starter/` into a scratch directory and runs `python3 range_query.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m04l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
