# m07l04-03 · Knapsack tabulation: filling the DP table

**Lesson:** [Dynamic Programming: Memoisation And Tabulation](https://learnsome.tech/learn/algorithms-course/m07l04) (lesson 7.4, module 7: Problem-Solving Techniques) · Pro  
**Check:** Graded

## Goal

You can explain overlapping subproblems and optimal substructure, apply memoisation with lru_cache to avoid redundant recursion, build a bottom-up tabulation table for the knapsack problem, and reconstruct a longest common subsequence from its DP table.

In the lesson: The knapsack problem asks for the maximum total value of items that fit within a weight limit. Optimal substructure holds because the best selection for capacity w using items one through i either includes item i or it does not: in either case the remaining choice is optimal for a smaller subproblem.

The table of subproblem values has rows for items and columns for capacity. Row zero is all zeros because no items means no value. At each cell, you take the better of skipping item i entirely or including it: if including it fits, the value is the item's value plus the best achievable with the remaining capacity using only previous items.

Three items and a capacity of four produce a five-by-five table. Printing the table lets you trace how the optimum builds up. Each row adds one item to the consideration set. Row two shows a capacity of two admits item two alone for value four. Row three confirms the best combination for capacity four is also five.

## Files

- [`starter/knapsack.py`](starter/knapsack.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m07l04/m07l04-03/starter`
2. Read `knapsack.py` the way the lesson builds it:
   - Lines 1–11: table of subproblem values
   - Lines 12–15: three items and a capacity
   - Lines 16–21: each row adds one item
3. Run it: `python3 knapsack.py`.
4. Check it from the repository root: `./check m07l04-03`.

## Expected output

```text
     0  1  2  3  4
[0]  0  0  0  0  0
[1]  0  1  1  1  1
[2]  0  1  4  5  5
[3]  0  1  4  5  5
max value: 5
```

## How to check

`./check m07l04-03` copies `starter/` into a scratch directory and runs `python3 knapsack.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m07l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
