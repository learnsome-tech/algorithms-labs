# m01l03-03 · Reversing in place, reusing the same memory

**Lesson:** [Space, In-Place Work And The Call Stack](https://learnsome.tech/learn/algorithms-course/m01l03) (lesson 1.3, module 1: Complexity And Trade-offs) · Free  
**Check:** Graded

## Goal

You can distinguish auxiliary space from in-place algorithms, measure Python object sizes with sys.getsizeof, explain why deep recursion exhausts the call stack, and convert a recursive function to an iterative one.

In the lesson: The in-place reverse uses two pointers: left starts at the first element and right starts at the last. Each iteration swaps the two ends and moves the pointers toward the middle until they meet. The algorithm needs only two index variables no matter how long the list is: constant auxiliary space. Below, the same experiment runs with Python's built-in reverse method. The size measured before the reverse and the size measured after are identical: the list object stays the same size, because reversing rearranges existing references rather than creating new ones. In-place means exactly this: the algorithm lives inside the memory the input already occupies, and it stays the same size throughout.

## Files

- [`starter/reverse_inplace.py`](starter/reverse_inplace.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l03/m01l03-03/starter`
2. Read `reverse_inplace.py` the way the lesson builds it:
   - Lines 1–9: swaps the two ends
   - Lines 10–15: measured before the reverse
   - Lines 16–18: same size
3. Run it: `python3 reverse_inplace.py`.
4. Check it from the repository root: `./check m01l03-03`.

## Expected output

```text
reversed in place: [7, 6, 5, 4, 3, 2, 1, 0]
size before: 80056
size after: 80056
same size: True
```

## How to check

`./check m01l03-03` copies `starter/` into a scratch directory and runs `python3 reverse_inplace.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m01l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
