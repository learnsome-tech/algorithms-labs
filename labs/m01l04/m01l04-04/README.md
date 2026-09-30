# m01l04-04 · Watching the ratio with a simple function

**Lesson:** [Big O, Big Omega And Big Theta](https://learnsome.tech/learn/algorithms-course/m01l04) (lesson 1.4, module 1: Complexity And Trade-offs) · Free  
**Check:** Graded

## Goal

You can define big O, big Omega, and big Theta in words, verify an asymptotic claim empirically by checking the ratio of cost to n, and distinguish best, worst, and average case for linear search.

In the lesson: The shell puts the ratio test in your hands. The first function is three n plus five, a classic linear function with a leading constant and an additive term. Dividing its output by n gives three point five at ten, three point zero five at one hundred, and three point zero zero five at one thousand. The ratio is shrinking toward three: a finite limit, which is the definition of bounded growth. The second function is n squared. Dividing its output by n gives ten at ten, one hundred at one hundred, one thousand at one thousand. The ratio grows without bound. That is an unbounded ratio, which is why n squared cannot be order n no matter what constant you try.

## Files

- [`starter/shell-watching-the-ratio-with-a-simple-function.py`](starter/shell-watching-the-ratio-with-a-simple-function.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l04/m01l04-04/starter`
2. Read `shell-watching-the-ratio-with-a-simple-function.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   def f(n): return 3 * n + 5
   f(10) / 10
   f(100) / 100
   f(1000) / 1000
   def g(n): return n * n
   g(10) / 10
   g(100) / 100
   g(1000) / 1000
   ```
4. Run it: `python3 -i < shell-watching-the-ratio-with-a-simple-function.py`.
5. Check it from the repository root: `./check m01l04-04`.

## Expected output

```text
3.5
3.05
3.005
10.0
100.0
1000.0
```

## How to check

`./check m01l04-04` copies `starter/` into a scratch directory and runs `python3 -i < shell-watching-the-ratio-with-a-simple-function.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m01l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
