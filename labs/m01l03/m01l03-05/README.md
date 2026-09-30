# m01l03-05 · Converting recursion to iteration

**Lesson:** [Space, In-Place Work And The Call Stack](https://learnsome.tech/learn/algorithms-course/m01l03) (lesson 1.3, module 1: Complexity And Trade-offs) · Free  
**Check:** Graded

## Goal

You can distinguish auxiliary space from in-place algorithms, measure Python object sizes with sys.getsizeof, explain why deep recursion exhausts the call stack, and convert a recursive function to an iterative one.

In the lesson: The iterative version avoids the call stack entirely. Instead of calling itself, the function uses an accumulator pattern: a variable called total starts at zero and grows by adding each number in the range. There are no nested calls, no stack frames beyond the one the function itself occupies, and no limit on how large n can be. The three calls confirm it: ten produces fifty-five, matching the recursive version; two thousand succeeds where the recursive function crashed; and one million is computed without complaint. The iterative version also runs faster in Python because function call overhead is significant. The trade is losing the natural correspondence between the recursive code and the mathematical definition, but for deep sequences, the iterative version is the right choice.

## Files

- [`starter/iterative_sum.py`](starter/iterative_sum.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l03/m01l03-05/starter`
2. Read `iterative_sum.py` the way the lesson builds it:
   - Lines 1–5: accumulator pattern
   - Lines 6–9: one million
3. Run it: `python3 iterative_sum.py`.
4. Check it from the repository root: `./check m01l03-05`.

## Expected output

```text
sum of ten: 55
sum of two thousand: 2001000
sum of one million: 500000500000
```

## How to check

`./check m01l03-05` copies `starter/` into a scratch directory and runs `python3 iterative_sum.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m01l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
