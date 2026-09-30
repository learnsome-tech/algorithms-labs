# m07l02-02 · Interval scheduling: always pick the earliest finish

**Lesson:** [Greedy Algorithms: When Local Is Global](https://learnsome.tech/learn/algorithms-course/m07l02) (lesson 7.2, module 7: Problem-Solving Techniques) · Pro  
**Check:** Graded

## Goal

You can implement interval scheduling by earliest finish, explain why greedy coin change fails on some coin systems by comparing with the dynamic-programming optimum, and build a Huffman code using a priority queue.

In the lesson: Interval scheduling asks how many non-overlapping intervals you can select from a set. The greedy answer is always to pick the interval that finishes earliest: it frees up the most room for future intervals. Sort by finish time, set the last occupied end to negative infinity, then walk through and accept any interval that starts at or after the current end.

The exchange argument shows this is optimal. Suppose an optimal solution picks a different first interval with a later finish. Swap in the one that finishes earliest instead. Everything it enabled remains enabled, and you have not lost anything. The argument applies repeatedly until the greedy solution and the optimal solution agree.

For the eight meetings shown here, the function selects three: the one ending at four, the one from four to seven, and the one from eight to eleven. Printing each chosen interval and the total chosen confirms the selection.

## Files

- [`starter/intervals.py`](starter/intervals.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m07l02/m07l02-02/starter`
2. Read `intervals.py` the way the lesson builds it:
   - Lines 1–9: finishes earliest
   - Lines 10–15: printing each chosen
3. Run it: `python3 intervals.py`.
4. Check it from the repository root: `./check m07l02-02`.

## Expected output

```text
1 to 4
4 to 7
8 to 11
total chosen: 3
```

## How to check

`./check m07l02-02` copies `starter/` into a scratch directory and runs `python3 intervals.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m07l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
