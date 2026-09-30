# m01l04-02 · Checking an upper bound by watching the ratio

**Lesson:** [Big O, Big Omega And Big Theta](https://learnsome.tech/learn/algorithms-course/m01l04) (lesson 1.4, module 1: Complexity And Trade-offs) · Free  
**Check:** Graded

## Goal

You can define big O, big Omega, and big Theta in words, verify an asymptotic claim empirically by checking the ratio of cost to n, and distinguish best, worst, and average case for linear search.

In the lesson: A linear work function counts exactly one operation per element. Divided by n, the ratio is always one: the cost per element is constant. That bounded ratio is exactly what big O of n means. The quadratic work function has a nested loop, so it counts n squared operations for each input size. The ratio of cost to n is not one but n itself, growing by a factor of ten each row. A function whose cost divided by n grows without bound cannot be called order n. Running both at three sizes makes the contrast unmistakable: the linear ratio stays flat while the ratio grows by a factor of one hundred between the smallest and largest input. Constant ratio equals bounded growth equals a valid O of n claim.

## Files

- [`starter/ratio_check.py`](starter/ratio_check.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l04/m01l04-02/starter`
2. Read `ratio_check.py` the way the lesson builds it:
   - Lines 1–6: linear work function
   - Lines 7–12: nested loop
   - Lines 13–18: ratio grows by a factor
3. Run it: `python3 ratio_check.py`.
4. Check it from the repository root: `./check m01l04-02`.

## Expected output

```text
n       lin  lin/n  quad      quad/n
100 100 1 10000 100
1000 1000 1 1000000 1000
10000 10000 1 100000000 10000
```

## How to check

`./check m01l04-02` copies `starter/` into a scratch directory and runs `python3 ratio_check.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m01l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
