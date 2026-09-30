# m01l02-06 · Counting work in a sort-based algorithm

**Lesson:** [Recognising The Common Growth Rates](https://learnsome.tech/learn/algorithms-course/m01l02) (lesson 1.2, module 1: Complexity And Trade-offs) · Free  
**Check:** Graded

## Goal

You can name the five common growth rates, count operations for each pattern in code, and say which code structure produces which growth rate.

In the lesson: Sorting work is the canonical example of n log n complexity, and this program counts it directly. The function counts merge passes: for a list of n elements, a merge sort makes a number of passes equal to the ceiling of the base-two logarithm of n. Each pass visits all n elements. The outer loop visits four input sizes, doubling by a factor of eight each row. When n grows from eight to four thousand and ninety-six, the work grows from twenty-four to forty-nine thousand one hundred and fifty-two. The key observation: the work grows faster than n, because the number of passes grows with n, but much slower than n squared. That is the territory between linear and quadratic, where most practical sorting algorithms live.

## Files

- [`starter/sort_work.py`](starter/sort_work.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l02/m01l02-06/starter`
2. Read `sort_work.py` the way the lesson builds it:
   - Lines 1–9: counts merge passes
   - Lines 10–15: outer loop visits
3. Run it: `python3 sort_work.py`.
4. Check it from the repository root: `./check m01l02-06`.

## Expected output

```text
8 3 24
64 6 384
512 9 4608
4096 12 49152
```

## How to check

`./check m01l02-06` copies `starter/` into a scratch directory and runs `python3 sort_work.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m01l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
