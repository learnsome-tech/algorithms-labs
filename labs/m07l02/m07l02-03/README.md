# m07l02-03 · Coin change: greedy works for standard coins

**Lesson:** [Greedy Algorithms: When Local Is Global](https://learnsome.tech/learn/algorithms-course/m07l02) (lesson 7.2, module 7: Problem-Solving Techniques) · Pro  
**Check:** Graded

## Goal

You can implement interval scheduling by earliest finish, explain why greedy coin change fails on some coin systems by comparing with the dynamic-programming optimum, and build a Huffman code using a priority queue.

In the lesson: With the standard US denominations of one, five, ten, and twenty-five, the greedy strategy always gives the fewest coins. Sort the denominations from largest to smallest, then greedily subtract the biggest coin that still fits, repeating until the amount reaches zero.

For forty-one cents, the algorithm takes a twenty-five first, leaving sixteen. Then a ten, leaving six. Then a five, leaving one. Then a one. Four coins total, and no arrangement of these denominations can reach forty-one with fewer. The exchange argument works here because the denominations are structured in a way that prevents a large coin from ever blocking a better combination later. Four coins is the proof that the greedy approach produces the optimal answer.

## Files

- [`starter/coin_us.py`](starter/coin_us.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m07l02/m07l02-03/starter`
2. Read `coin_us.py` the way the lesson builds it:
   - Lines 1–8: greedily subtract
   - Lines 9–12: the algorithm takes
3. Run it: `python3 coin_us.py`.
4. Check it from the repository root: `./check m07l02-03`.

## Expected output

```text
coins used: [25, 10, 5, 1]
total: 4 coins
```

## How to check

`./check m07l02-03` copies `starter/` into a scratch directory and runs `python3 coin_us.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m07l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
