# m01l03-04 · Recursion and the call stack

**Lesson:** [Space, In-Place Work And The Call Stack](https://learnsome.tech/learn/algorithms-course/m01l03) (lesson 1.3, module 1: Complexity And Trade-offs) · Free  
**Check:** Graded

## Goal

You can distinguish auxiliary space from in-place algorithms, measure Python object sizes with sys.getsizeof, explain why deep recursion exhausts the call stack, and convert a recursive function to an iterative one.

In the lesson: Recursive functions consume stack frames: each call to recursive sum opens a frame that holds the local variables, the return address, and the current value of n. The base case at n equal to zero ends the chain. Python's default recursion limit is one thousand frames, and the function confirms it works at ten: returning fifty-five, the correct sum of zero through ten. The recursion limit setting can be read from the sys module and is one thousand by default. When we attempt to compute the sum all the way to two thousand, Python raises a RecursionError rather than silently overflowing the stack. Each open frame on the call stack occupies memory, so the space cost of a recursive function is proportional to the maximum depth of the recursion.

## Files

- [`starter/recursive_sum.py`](starter/recursive_sum.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l03/m01l03-04/starter`
2. Read `recursive_sum.py` the way the lesson builds it:
   - Lines 1–6: base case
   - Lines 7–9: recursion limit
   - Lines 10–15: two thousand
3. Run it: `python3 recursive_sum.py`.
4. Check it from the repository root: `./check m01l03-04`.

## Expected output

```text
sum of ten: 55
recursion limit: 1000
two thousand: RecursionError
```

## How to check

`./check m01l03-04` copies `starter/` into a scratch directory and runs `python3 recursive_sum.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m01l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
