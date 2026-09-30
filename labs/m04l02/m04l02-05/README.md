# m04l02-05 · When key range becomes the bottleneck

**Lesson:** [Counting And Radix Sort: Beating N Log N](https://learnsome.tech/learn/algorithms-course/m04l02) (lesson 4.2, module 4: Sorting And Searching) · Pro  
**Check:** Graded

## Goal

You can implement counting sort and LSD radix sort, explain when each applies, and describe the memory cost that comes with bypassing element comparisons.

In the lesson: The small-range sort works perfectly on the ten-element digit example. The memory column tells a different story: each possible key value needs one pointer-sized slot in the count array, which on a sixty-four-bit system is eight bytes. For a key range of ten that is negligible, eighty bytes total. For a key range of one hundred thousand it is eight hundred thousand bytes, almost one megabyte, consumed before a single element has been read. For keys that are general Unicode strings, the key range reaches into the billions and counting sort becomes impractical. Radix sort addresses larger ranges by treating the key as several smaller digits, but even it faces limits when the digit alphabet is very large. Comparison-based sorts win precisely in these cases because they need no auxiliary memory proportional to the key range.

## Files

- [`starter/limits.py`](starter/limits.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l02/m04l02-05/starter`
2. Read `limits.py`.
3. Run it: `python3 limits.py`.
4. Check it from the repository root: `./check m04l02-05`.

## Expected output

```text
small range: [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]
k=10: count array needs 80 bytes
k=100: count array needs 800 bytes
k=100000: count array needs 800000 bytes
```

## How to check

`./check m04l02-05` copies `starter/` into a scratch directory and runs `python3 limits.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m04l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
