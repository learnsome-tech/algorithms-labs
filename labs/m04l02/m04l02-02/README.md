# m04l02-02 · Counting sort: one pass to count, one to reconstruct

**Lesson:** [Counting And Radix Sort: Beating N Log N](https://learnsome.tech/learn/algorithms-course/m04l02) (lesson 4.2, module 4: Sorting And Searching) · Pro  
**Check:** Graded

## Goal

You can implement counting sort and LSD radix sort, explain when each applies, and describe the memory cost that comes with bypassing element comparisons.

In the lesson: Counting sort takes k as a second argument, the exclusive upper bound on the key values. The first loop allocates k zero counters and then the count then reconstruct pass reads the input once, incrementing the counter at index v for each value v encountered. The second loop walks the count array in order and extends the result list with v copies of the value v. No element is ever compared with another element: the sort is comparison-free. The random input has twelve values in the range zero through nine, and the output confirms that seven appears four times and one appears three times. The verified line at the end checks that the result matches the built-in sort. Notice that the output comes out in non-decreasing order even though the input was shuffled; the algorithm reads the count array from left to right, so values emerge in sorted order automatically.

## Files

- [`starter/counting_sort.py`](starter/counting_sort.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l02/m04l02-02/starter`
2. Read `counting_sort.py` the way the lesson builds it:
   - Lines 1–8: count then reconstruct
   - Lines 9–16: output confirms
3. Run it: `python3 counting_sort.py`.
4. Check it from the repository root: `./check m04l02-02`.

## Expected output

```text
input:  [2, 9, 1, 4, 1, 7, 7, 7, 6, 3, 1, 7]
sorted: [1, 1, 1, 2, 3, 4, 6, 7, 7, 7, 7, 9]
verified: True
```

## How to check

`./check m04l02-02` copies `starter/` into a scratch directory and runs `python3 counting_sort.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m04l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
