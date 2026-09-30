# m01l03-02 · Building a reversed copy and measuring list sizes

**Lesson:** [Space, In-Place Work And The Call Stack](https://learnsome.tech/learn/algorithms-course/m01l03) (lesson 1.3, module 1: Complexity And Trade-offs) · Free  
**Check:** Graded

## Goal

You can distinguish auxiliary space from in-place algorithms, measure Python object sizes with sys.getsizeof, explain why deep recursion exhausts the call stack, and convert a recursive function to an iterative one.

In the lesson: Reversing a list with slice notation creates a brand new list. Original holds the values zero through four, and the reversed copy holds them in the opposite order. The last print confirms the original is unchanged: the slice built an entirely separate object. Below that, three lists of growing length are built and their byte sizes measured with getsizeof. The bytes each list occupies grow in proportion to the element count, confirming that the slice-based reverse allocates space proportional to n. That is linear auxiliary space: for every element in the input, the algorithm claims a corresponding slot in the new copy. For small lists that cost is negligible; for lists of millions of items, the allocation cost becomes the bottleneck.

## Files

- [`starter/reverse_copy.py`](starter/reverse_copy.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l03/m01l03-02/starter`
2. Read `reverse_copy.py` the way the lesson builds it:
   - Lines 1–4: slice notation
   - Lines 5–7: original is unchanged
   - Lines 8–12: bytes each list
3. Run it: `python3 reverse_copy.py`.
4. Check it from the repository root: `./check m01l03-02`.

## Expected output

```text
original: [0, 1, 2, 3, 4]
reversed: [4, 3, 2, 1, 0]
original unchanged: [0, 1, 2, 3, 4]
100 856
1000 8056
10000 80056
```

## How to check

`./check m01l03-02` copies `starter/` into a scratch directory and runs `python3 reverse_copy.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m01l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
