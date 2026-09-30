# m04l04-05 · K-way external merge with heapq.merge

**Lesson:** [Sorting In Real Systems: Stability, Keys And External Sort](https://learnsome.tech/learn/algorithms-course/m04l04) (lesson 4.4, module 4: Sorting And Searching) · Pro  
**Check:** Graded

## Goal

You can sort with key functions and tuple keys, compose sorts by chaining stable passes, and implement a k-way external merge using heapq.merge over temporary files.

In the lesson: An external sort handles datasets too large to fit in memory. The standard approach writes sorted chunks to temporary files and merges them in one pass. This segment shows the merge phase. The setup loop writes three sorted chunk files to the working directory. The merge opens all three files at once, wraps each file handle with an integer conversion iterator, and passes all three iterators to heapq dot merge. The heapq dot merge function reads one value at a time from whichever input is currently smallest, using a heap to track the minimum, so total memory at any moment is proportional to the number of chunks, not to the total data size. After the verified output appears you close all file handles. In production you would also delete the temporary chunk files after the merge completes successfully.

## Files

- [`starter/chunk0.txt`](starter/chunk0.txt)
- [`starter/chunk1.txt`](starter/chunk1.txt)
- [`starter/chunk2.txt`](starter/chunk2.txt)
- [`starter/external_sort.py`](starter/external_sort.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l04/m04l04-05/starter`
2. Read `external_sort.py` the way the lesson builds it:
   - Lines 1–12: three sorted chunk files
   - Lines 13–17: verified output appears
3. Run it: `python3 external_sort.py`.
4. Check it from the repository root: `./check m04l04-05`.

## Expected output

```text
merged: [3, 12, 18, 24, 35, 42, 55, 56, 67, 78, 89, 91]
verified: True
```

## How to check

`./check m04l04-05` copies `starter/` into a scratch directory and runs `python3 external_sort.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m04l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
