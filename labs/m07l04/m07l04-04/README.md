# m07l04-04 · Longest common subsequence with reconstruction

**Lesson:** [Dynamic Programming: Memoisation And Tabulation](https://learnsome.tech/learn/algorithms-course/m07l04) (lesson 7.4, module 7: Problem-Solving Techniques) · Pro  
**Check:** Graded

## Goal

You can explain overlapping subproblems and optimal substructure, apply memoisation with lru_cache to avoid redundant recursion, build a bottom-up tabulation table for the knapsack problem, and reconstruct a longest common subsequence from its DP table.

In the lesson: The longest common subsequence of two strings is the longest sequence of characters that appears in both, in order, but not necessarily contiguously. Filling the length table follows a simple rule: if the current characters match, extend the longest subsequence found without either character; otherwise take the better of skipping a character from one string or the other.

The table alone gives only the length. Tracing back through the table from the bottom-right corner recovers the actual subsequence. At each cell, if the characters matched, this character is part of the answer and both indices move back by one. If they did not match, move in the direction of the larger neighbour.

For the strings shown here, printing the reconstructed subsequence gives four characters: the letters that appear in both strings in the right relative order, chosen to maximise length.

## Files

- [`starter/lcs.py`](starter/lcs.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m07l04/m07l04-04/starter`
2. Read `lcs.py` the way the lesson builds it:
   - Lines 1–7: filling the length table
   - Lines 8–13: tracing back through
   - Lines 14–17: printing the reconstructed
3. Run it: `python3 lcs.py`.
4. Check it from the repository root: `./check m07l04-04`.

## Expected output

```text
LCS length: 4
LCS: BDAB
```

## How to check

`./check m07l04-04` copies `starter/` into a scratch directory and runs `python3 lcs.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m07l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
