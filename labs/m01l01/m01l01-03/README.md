# m01l01-03 · Measuring the gap with a timer

**Lesson:** [Why Complexity Matters In Production](https://learnsome.tech/learn/algorithms-course/m01l01) (lesson 1.1, module 1: Complexity And Trade-offs) · Free  
**Check:** Graded

## Goal

You can explain why scanning a list grows linearly with input size while a dictionary lookup stays constant, measure both with the perf counter timer, and describe what input size n means in a complexity argument.

In the lesson: Real code cannot introspect its own complexity, but head-to-head measurement reveals the difference clearly. This program builds ten thousand users as both a list and a dict, placing the search target at the very end so the list must always scan all the way through. The perf counter function from the time module gives sub-microsecond resolution and is not affected by wall-clock drift. The list timing loop runs the membership test a thousand times and records the elapsed cost. The dict timing loop does the same, but each test jumps straight to the bucket. Finally the program prints two comparisons: the dict was faster, and the ratio above five confirms the advantage is not noise. Both will hold on any machine once the list is long enough to matter.

## Files

- [`starter/handler_timing.py`](starter/handler_timing.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l01/m01l01-03/starter`
2. Read `handler_timing.py` the way the lesson builds it:
   - Lines 1–7: ten thousand users
   - Lines 8–12: list timing loop
   - Lines 13–17: dict timing loop
   - Lines 18–20: ratio above five
3. Run it: `python3 handler_timing.py`.
4. Check it from the repository root: `./check m01l01-03`.

## Expected output

```text
dict lookup was faster: True
ratio above five: True
```

## How to check

`./check m01l01-03` copies `starter/` into a scratch directory and runs `python3 handler_timing.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m01l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
