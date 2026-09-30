# m03l01-03 · Verifying constant-time index access

**Lesson:** [Arrays: Contiguous Memory And Constant-Time Access](https://learnsome.tech/learn/algorithms-course/m03l01) (lesson 3.1, module 3: Sequences: Arrays, Lists, Stacks And Queues) · Pro  
**Check:** Runs, not graded

## Goal

You can explain why array index access is constant time, measure the memory difference between a typed array and a list, predict the cost of front insertion versus appending, and describe why slicing produces a copy.

In the lesson: The claim that index access costs constant time is worth measuring rather than just accepting. This program creates a list of one hundred thousand integers and times fifty thousand reads from position zero, then fifty thousand reads from the very last position. If index access were proportional to the position, the ratio of the two timings would be large; instead, the ratio should be close to one, because the lookup is arithmetic regardless of where in the array the slot lives. The program bounds the ratio between a lower and an upper threshold to confirm the two timings are within the same order of magnitude. When the ratio falls inside that window, you see it confirmed by printing a single boolean. Varying the list size or the number of reads does not change the conclusion; only the clock values shift.

## Files

- [`starter/consttime.py`](starter/consttime.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l01/m03l01-03/starter`
2. Read `consttime.py` the way the lesson builds it:
   - Lines 1–2: This program creates a list
   - Lines 3–9: fifty thousand reads from position zero
   - Lines 10–11: The program bounds
3. Run it: `python3 consttime.py`.
4. Check it from the repository root: `./check m03l01-03`.

## What the lesson recorded

Shown for reference; the check does not compare it.

```text
constant-time access confirmed: True
```

## How to check

`./check m03l01-03` copies `starter/` into a scratch directory and runs `python3 consttime.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It runs without a pass or fail: what the listing prints in the lab sandbox differs from the output recorded for the lesson (it depends on the machine, the clock or the network), so the site runs it without a pass or fail. `./check` shows the output and the exit code.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m03l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
