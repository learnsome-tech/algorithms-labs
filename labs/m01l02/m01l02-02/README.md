# m01l02-02 · A growth table from counted operations

**Lesson:** [Recognising The Common Growth Rates](https://learnsome.tech/learn/algorithms-course/m01l02) (lesson 1.2, module 1: Complexity And Trade-offs) · Free  
**Check:** Graded

## Goal

You can name the five common growth rates, count operations for each pattern in code, and say which code structure produces which growth rate.

In the lesson: The program imports the math module for its logarithm function, then prints a header row labelling the columns: n, constant, log n, linear, n times log n, and quadratic. The loop runs at four sizes: ten, one hundred, one thousand, and ten thousand. For constant time, the count is always one, independent of n. For log n, the floor of the binary logarithm gives the number of halving steps needed. Linear is just n itself. N times log n is the product. Look at what happens to the quadratic column as n grows by a factor of ten: the count grows by a factor of one hundred. Four sizes make the pattern clear. That squared relationship is what makes quadratic algorithms impractical at large scale even on fast hardware.

## Files

- [`starter/growth_table.py`](starter/growth_table.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l02/m01l02-02/starter`
2. Read `growth_table.py` the way the lesson builds it:
   - Lines 1: math module
   - Lines 2–4: header row
   - Lines 5–7: four sizes
3. Run it: `python3 growth_table.py`.
4. Check it from the repository root: `./check m01l02-02`.

## Expected output

```text
n        const  logn  linear  nlogn      quad
10 1 3 10 30 100
100 1 6 100 600 10000
1000 1 9 1000 9000 1000000
10000 1 13 10000 130000 100000000
```

## How to check

`./check m01l02-02` copies `starter/` into a scratch directory and runs `python3 growth_table.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m01l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
