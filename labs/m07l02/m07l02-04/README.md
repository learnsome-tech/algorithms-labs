# m07l02-04 · Coin change: greedy fails on arbitrary denominations

**Lesson:** [Greedy Algorithms: When Local Is Global](https://learnsome.tech/learn/algorithms-course/m07l02) (lesson 7.2, module 7: Problem-Solving Techniques) · Pro  
**Check:** Graded

## Goal

You can implement interval scheduling by earliest finish, explain why greedy coin change fails on some coin systems by comparing with the dynamic-programming optimum, and build a Huffman code using a priority queue.

In the lesson: Change the coin system to one, three, and four, and ask for six. The same greedy function picks the four first, leaving two, then takes two ones: three coins. But six equals three plus three, which is only two coins.

Greedy fails here because taking the four is locally attractive but globally wasteful. The dynamic programming solution fills a table from zero up to the target amount, asking for each cell: what is the fewest coins needed to reach this total? It considers every denomination at every cell, so it always finds the true minimum.

The contrast becomes clear in the output: greedy reports three, dynamic programming reports two. No exchange argument saves the greedy approach on this coin system. The denominations are not structured in a way that makes the locally largest choice globally safe. When the greedy-choice property fails, dynamic programming is the fallback.

## Files

- [`starter/coin_fail.py`](starter/coin_fail.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m07l02/m07l02-04/starter`
2. Read `coin_fail.py` the way the lesson builds it:
   - Lines 1–8: same greedy function
   - Lines 9–17: dynamic programming
   - Lines 18–22: contrast becomes clear
3. Run it: `python3 coin_fail.py`.
4. Check it from the repository root: `./check m07l02-04`.

## Expected output

```text
greedy: [4, 1, 1] coins used: 3
optimal count: 2
```

## How to check

`./check m07l02-04` copies `starter/` into a scratch directory and runs `python3 coin_fail.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m07l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
