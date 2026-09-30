# m01l02-04 · Halving and the logarithm

**Lesson:** [Recognising The Common Growth Rates](https://learnsome.tech/learn/algorithms-course/m01l02) (lesson 1.2, module 1: Complexity And Trade-offs) · Free  
**Check:** Graded

## Goal

You can name the five common growth rates, count operations for each pattern in code, and say which code structure produces which growth rate.

In the lesson: The shell session makes the log growth pattern concrete. Start with n equal to one thousand and twenty-four, which is two to the tenth power. A while loop divides by two on each iteration and counts the divisions. After the loop, steps is ten: it took exactly ten halvings to bring the number to one. The second example starts with two to the twentieth power. The count reaches twenty. Multiplying n by itself a million times adds only ten steps. That is what logarithmic growth means: the work grows so slowly that multiplying n by any power of two adds only one step per power. No realistic data size can make a logarithmic algorithm slow.

## Files

- [`starter/shell-halving-and-the-logarithm.py`](starter/shell-halving-and-the-logarithm.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l02/m01l02-04/starter`
2. Read `shell-halving-and-the-logarithm.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   n = 1024
   steps = 0
   while n > 1: n //= 2; steps += 1
   steps
   n = 1048576
   steps = 0
   while n > 1: n //= 2; steps += 1
   steps
   ```
4. Run it: `python3 -i < shell-halving-and-the-logarithm.py`.
5. Check it from the repository root: `./check m01l02-04`.

## Expected output

```text
10
20
```

## How to check

`./check m01l02-04` copies `starter/` into a scratch directory and runs `python3 -i < shell-halving-and-the-logarithm.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m01l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
