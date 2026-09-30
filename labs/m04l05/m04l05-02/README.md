# m04l05-02 · Membership speed: set, bisect, and linear scan

**Lesson:** [Searching With Hashes Versus Trees](https://learnsome.tech/learn/algorithms-course/m04l05) (lesson 4.5, module 4: Sorting And Searching) · Pro  
**Check:** Graded

## Goal

You can choose between a set, a sorted list with bisect, and a linear scan for membership and range queries, and explain when sorted order provides capabilities that hashing cannot.

In the lesson: The measurement targets the last element in a sorted list of one hundred thousand integers, the worst case for linear search and a representative case for the others. All three lookup functions chase the same target so the comparison is fair. The time-it helper repeats each lookup two thousand times and measures the total wall time, reducing timing noise from the operating system. Linear scan gets only twenty repetitions because it is much slower than the others. The three lookup functions are timed: the set membership operator, a bisect-left call followed by an index check, and the plain in operator on the list. Both lines print True on any machine because constant-time hashing and logarithmic bisection are both enormously faster than scanning one hundred thousand elements. Only booleans are printed, not raw timings, because timings depend on hardware and would not reproduce exactly.

## Files

- [`starter/membership.py`](starter/membership.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l05/m04l05-02/starter`
2. Read `membership.py` the way the lesson builds it:
   - Lines 1–14: three lookup functions
   - Lines 15–19: both lines print True
3. Run it: `python3 membership.py`.
4. Check it from the repository root: `./check m04l05-02`.

## Expected output

```text
set faster than linear: True
bisect faster than linear: True
```

## How to check

`./check m04l05-02` copies `starter/` into a scratch directory and runs `python3 membership.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m04l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
