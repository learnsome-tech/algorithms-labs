# m07l05-03 · Capstone: one problem solved three ways

**Lesson:** [Recognising The Pattern](https://learnsome.tech/learn/algorithms-course/m07l05) (lesson 7.5, module 7: Problem-Solving Techniques) · Pro  
**Check:** Graded

## Goal

You can apply a four-question decision procedure to classify an unfamiliar problem as divide-and-conquer, greedy, backtracking, or dynamic programming, implement a rule-table classifier in Python, and verify that three approaches to the same problem agree on the answer.

In the lesson: Coin change with US denominations admits all three deterministic approaches. The greedy pass subtracts the largest fitting denomination at each step, completing the change in one loop. This works here because the US denomination structure has the greedy-choice property.

Memoised recursion asks: what is the fewest coins for this amount? If zero, done. Otherwise try subtracting each denomination and take one plus the minimum of the recursive results. The memoisation cache stores each amount once computed, so every recursive call beyond the first is free.

Tabulation fills a table from one up to the target amount, using the same recurrence but iteratively. The result at each index is one more than the best reachable by subtracting each denomination.

All three agree on the answer for each test amount, which is the expected outcome when the greedy-choice property holds. The label printed next to each result confirms agreement and would flag any divergence for investigation.

## Files

- [`starter/three_ways.py`](starter/three_ways.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m07l05/m07l05-03/starter`
2. Read `three_ways.py` the way the lesson builds it:
   - Lines 1–7: greedy pass
   - Lines 8–12: memoised recursion
   - Lines 13–18: tabulation fills
   - Lines 19–22: all three agree
3. Run it: `python3 three_ways.py`.
4. Check it from the repository root: `./check m07l05-03`.

## Expected output

```text
amount 11: 2 coins [agree]
amount 30: 2 coins [agree]
amount 41: 4 coins [agree]
```

## How to check

`./check m07l05-03` copies `starter/` into a scratch directory and runs `python3 three_ways.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m07l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
