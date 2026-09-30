# m04l05-05 · Summary table: operations across three structures

**Lesson:** [Searching With Hashes Versus Trees](https://learnsome.tech/learn/algorithms-course/m04l05) (lesson 4.5, module 4: Sorting And Searching) · Pro  
**Check:** Graded

## Goal

You can choose between a set, a sorted list with bisect, and a linear scan for membership and range queries, and explain when sorted order provides capabilities that hashing cannot.

In the lesson: The table summarises the complexity comparison across the three structures for the five operations that come up most in practice. Sets win on membership, insert, and delete because hashing is constant in the expected case. Sorted lists win on range queries and on producing elements in sorted order: range query costs order log n plus k where k is the number of results, and iterating in sorted order is linear, whereas a set must sort its contents first, costing order n log n. An unsorted list is competitive only when data arrives in order, is rarely searched, or the element count is so small that the constant factors of hashing cost more than a linear scan. The table summarises the principle: structure your data in the order you plan to query it, and the right operation becomes cheap.

## Files

- [`starter/summary.py`](starter/summary.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l05/m04l05-05/starter`
2. Read `summary.py`.
3. Run it: `python3 summary.py`.
4. Check it from the repository root: `./check m04l05-05`.

## Expected output

```text
operation              set/dict   sorted list   linear
-----------------------------------------------------
membership                 O(1)      O(log n)     O(n)
insert                     O(1)          O(n)     O(n)
delete                     O(1)          O(n)     O(n)
range query                O(n)  O(log n + k)     O(n)
sorted walk          O(n log n)          O(n)     O(n)
```

## How to check

`./check m04l05-05` copies `starter/` into a scratch directory and runs `python3 summary.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m04l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
