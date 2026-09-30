# m07l05-04 · Verifying greedy equals optimal across a range

**Lesson:** [Recognising The Pattern](https://learnsome.tech/learn/algorithms-course/m07l05) (lesson 7.5, module 7: Problem-Solving Techniques) · Pro  
**Check:** Graded

## Goal

You can apply a four-question decision procedure to classify an unfamiliar problem as divide-and-conquer, greedy, backtracking, or dynamic programming, implement a rule-table classifier in Python, and verify that three approaches to the same problem agree on the answer.

In the lesson: A claim that greedy equals optimal for US coins should be checked, not assumed. The verification program runs both approaches on every amount from one to ninety-nine and flags any discrepancy.

The greedy helper loops over denominations from largest to smallest, accumulating a count. The DP helper fills a table from zero to the target using the standard coin-change recurrence. Both functions are compact because neither needs to construct the actual coin list, only the count.

Checking every amount in the range and counting mismatches is more convincing than spot-checking a few values. The output confirms zero mismatches across ninety-nine test cases, consistent with the known mathematical property of the US denomination system. For the counterexample coins from the earlier lesson, the same test would report mismatches at several amounts, showing the difference between a verified claim and an assumption.

## Files

- [`starter/verify_coins.py`](starter/verify_coins.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m07l05/m07l05-04/starter`
2. Read `verify_coins.py` the way the lesson builds it:
   - Lines 1–5: greedy helper
   - Lines 6–11: DP helper fills
   - Lines 12–19: checking every amount
3. Run it: `python3 verify_coins.py`.
4. Check it from the repository root: `./check m07l05-04`.

## Expected output

```text
tested one to ninety-nine
mismatches found: 0
```

## How to check

`./check m07l05-04` copies `starter/` into a scratch directory and runs `python3 verify_coins.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m07l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
