# m01l02-03 · Counting nested loop and halving operations

**Lesson:** [Recognising The Common Growth Rates](https://learnsome.tech/learn/algorithms-course/m01l02) (lesson 1.2, module 1: Complexity And Trade-offs) · Free  
**Check:** Graded

## Goal

You can name the five common growth rates, count operations for each pattern in code, and say which code structure produces which growth rate.

In the lesson: The two functions make the counting explicit. The first function counts every pair of indices in an n by n grid: two nested for loops each running to n, so the total is n squared. The function does not do any useful work; it counts so the relationship is unmistakable. The second function counts each halving step: it starts with n and divides by two until it reaches one. That count is the floor of the base-two logarithm of n. The loop runs for three values of n. Eight pairs take sixty-four operations but only three halving steps. Five hundred and twelve pairs take more than a quarter million operations but only nine steps. The contrast between the second and third columns is the contrast between logarithmic and quadratic growth made concrete.

## Files

- [`starter/nested_count.py`](starter/nested_count.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l02/m01l02-03/starter`
2. Read `nested_count.py` the way the lesson builds it:
   - Lines 1–6: counts every pair
   - Lines 7–13: counts each halving
   - Lines 14–17: three values of n
3. Run it: `python3 nested_count.py`.
4. Check it from the repository root: `./check m01l02-03`.

## Expected output

```text
8 3 64
64 6 4096
512 9 262144
```

## How to check

`./check m01l02-03` copies `starter/` into a scratch directory and runs `python3 nested_count.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m01l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
