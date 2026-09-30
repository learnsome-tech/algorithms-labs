# m01l05-02 · A dynamic array that counts its copies

**Lesson:** [Amortised Analysis: Why Append Is Cheap](https://learnsome.tech/learn/algorithms-course/m01l05) (lesson 1.5, module 1: Complexity And Trade-offs) · Free  
**Check:** Graded

## Goal

You can explain why appending to a dynamic array is amortised constant time by tracing the doubling strategy, compare it to fixed-increment growth, and state the credit argument for the amortised bound.

In the lesson: The class on screen is a minimal dynamic array that tracks its own copy cost. When the length reaches the current capacity, the class records the copy count, then doubles its capacity and continues. No actual data is moved; the program counts what it would copy. Sixteen appends are performed: the capacity starts at one and doubles four times, ending at sixteen. The total copies is fifteen: one element copied on the first doubling, then two, then four, then eight. The average copies across all sixteen appends is less than one, confirming the amortised constant. An expensive copy at the moment of growth is balanced by many free appends that followed it, and the accounting works out to less than one copy per operation.

## Files

- [`starter/dynamic_array.py`](starter/dynamic_array.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l05/m01l05-02/starter`
2. Read `dynamic_array.py` the way the lesson builds it:
   - Lines 1–11: doubles its capacity
   - Lines 12–15: sixteen appends
   - Lines 16–19: average copies
3. Run it: `python3 dynamic_array.py`.
4. Check it from the repository root: `./check m01l05-02`.

## Expected output

```text
appended: 16
capacity: 16
total copies: 15
average copies: 0.9375
```

## How to check

`./check m01l05-02` copies `starter/` into a scratch directory and runs `python3 dynamic_array.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m01l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
