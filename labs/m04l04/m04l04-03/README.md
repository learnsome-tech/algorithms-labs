# m04l04-03 · Tuple keys for multi-column sorting

**Lesson:** [Sorting In Real Systems: Stability, Keys And External Sort](https://learnsome.tech/learn/algorithms-course/m04l04) (lesson 4.4, module 4: Sorting And Searching) · Pro  
**Check:** Graded

## Goal

You can sort with key functions and tuple keys, compose sorts by chaining stable passes, and implement a k-way external merge using heapq.merge over temporary files.

In the lesson: A single sorted call with a tuple key achieves multi-column sorting because tuples compare left-to-right: if the first element of two tuples is equal, Python moves on to the second, and so on. The employee records hold name, department, and score. The key lambda returns a three-element tuple: the department string for ascending order, the negated score for descending order because there is no direct way to reverse one column in a tuple key, and the name for a tiebreaker. Negating an integer flips its sort direction within a tuple key. The table prints showing engineering before marketing, and within engineering the highest score first: carol at ninety, then alice and eve tied at eighty-five in their original input order because stable sort preserves input order for identical keys. The pattern scales to any number of columns without extra passes.

## Files

- [`starter/multikey.py`](starter/multikey.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l04/m04l04-03/starter`
2. Read `multikey.py` the way the lesson builds it:
   - Lines 1–7: employee records
   - Lines 8–13: the table prints
3. Run it: `python3 multikey.py`.
4. Check it from the repository root: `./check m04l04-03`.

## Expected output

```text
dept asc, score desc, name asc:
  carol    eng  90
  alice    eng  85
  eve      eng  85
  bob      mkt  90
  dave     mkt  85
```

## How to check

`./check m04l04-03` copies `starter/` into a scratch directory and runs `python3 multikey.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m04l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
