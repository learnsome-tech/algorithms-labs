# m07l04-05 · Edit distance: insertions, deletions and substitutions

**Lesson:** [Dynamic Programming: Memoisation And Tabulation](https://learnsome.tech/learn/algorithms-course/m07l04) (lesson 7.4, module 7: Problem-Solving Techniques) · Pro  
**Check:** Graded

## Goal

You can explain overlapping subproblems and optimal substructure, apply memoisation with lru_cache to avoid redundant recursion, build a bottom-up tabulation table for the knapsack problem, and reconstruct a longest common subsequence from its DP table.

In the lesson: Edit distance counts the minimum number of single-character operations needed to convert one string to another: insert a character, delete a character, or substitute one character for another. Each operation costs one.

The base cases fill the first row and first column: converting an empty string to a string of length j costs j insertions; converting a string of length i to an empty string costs i deletions. At interior cells, if the characters match, no operation is needed and the cost equals the diagonal neighbour. If they differ, three operations correspond to three neighbours: delete from the first string, insert into the first string, or substitute. Take the minimum of the three and add one.

Three pairs demonstrate the table. Converting kitten to sitting costs three edits. Converting sunday to saturday also costs three, despite the strings looking quite different. Identical strings cost zero.

## Files

- [`starter/editdist.py`](starter/editdist.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m07l04/m07l04-05/starter`
2. Read `editdist.py` the way the lesson builds it:
   - Lines 1–7: base cases fill
   - Lines 8–15: three operations correspond
   - Lines 16–20: three pairs demonstrate
3. Run it: `python3 editdist.py`.
4. Check it from the repository root: `./check m07l04-05`.

## Expected output

```text
edit_dist('kitten', 'sitting') = 3
edit_dist('sunday', 'saturday') = 3
edit_dist('abc', 'abc') = 0
```

## How to check

`./check m07l04-05` copies `starter/` into a scratch directory and runs `python3 editdist.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m07l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
