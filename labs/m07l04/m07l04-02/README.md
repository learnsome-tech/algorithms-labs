# m07l04-02 · Fibonacci: naive recursion versus memoised recursion

**Lesson:** [Dynamic Programming: Memoisation And Tabulation](https://learnsome.tech/learn/algorithms-course/m07l04) (lesson 7.4, module 7: Problem-Solving Techniques) · Pro  
**Check:** Graded

## Goal

You can explain overlapping subproblems and optimal substructure, apply memoisation with lru_cache to avoid redundant recursion, build a bottom-up tabulation table for the knapsack problem, and reconstruct a longest common subsequence from its DP table.

In the lesson: Fibonacci is the simplest illustration of overlapping subproblems. To compute the twentieth Fibonacci number, naive recursion recomputes the nineteenth twice, the eighteenth four times, the seventeenth eight times, and so on. Each level roughly doubles the call count, giving exponential growth.

The cache decorator wraps the memoised version. On the first call to any argument, the result is computed and stored. Every subsequent call to the same argument returns the cached result immediately without recursing further. The function body is identical: the only change is adding the decorator.

Comparing call counts shows the dramatic difference. The naive version makes twenty-one thousand eight hundred and ninety-one calls to compute the twentieth Fibonacci number. The memoised version makes exactly twenty-one calls: one for each value from zero to twenty, because each value is computed at most once and then looked up from the cache.

## Files

- [`starter/fib_memo.py`](starter/fib_memo.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m07l04/m07l04-02/starter`
2. Read `fib_memo.py` the way the lesson builds it:
   - Lines 1–8: naive recursion recomputes
   - Lines 9–15: cache decorator
   - Lines 16–22: comparing call counts
3. Run it: `python3 fib_memo.py`.
4. Check it from the repository root: `./check m07l04-02`.

## Expected output

```text
fib(20) = 6765
naive calls: 21891
memo calls: 21
```

## How to check

`./check m07l04-02` copies `starter/` into a scratch directory and runs `python3 fib_memo.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m07l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
