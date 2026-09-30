# m04l01-06 · Stability: keeping equal elements in order

**Lesson:** [Comparison Sorts: Insertion, Merge And Quicksort](https://learnsome.tech/learn/algorithms-course/m04l01) (lesson 4.1, module 4: Sorting And Searching) · Pro  
**Check:** Graded

## Goal

You can implement insertion sort, merge sort, and quicksort with comparison counters, explain why no comparison sort beats order n log n, and demonstrate stability with tagged pairs.

In the lesson: Stability means that equal elements keep their original left-to-right order after sorting. The five pairs each have a numeric key and a letter tag. After sorting by key alone, elements with the same key must preserve their input order: x before y for key one, and b before a for key three. Insertion sort achieves stability through the strict greater than comparison in the while condition: the inner loop shifts a left neighbor only when it is strictly larger, never when it is equal, so tied elements stay put. Python's built-in sorted function also guarantees stability, and the order matches line confirms that both produce identical output. Stability matters because it lets you compose sorts: sort by a secondary criterion first, then by a primary criterion, and the primary sort leaves the secondary ordering intact within each primary group.

## Files

- [`starter/stability.py`](starter/stability.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l01/m04l01-06/starter`
2. Read `stability.py` the way the lesson builds it:
   - Lines 1–10: strict greater than comparison
   - Lines 11–16: order matches
3. Run it: `python3 stability.py`.
4. Check it from the repository root: `./check m04l01-06`.

## Expected output

```text
insertion sort: [(1, 'x'), (1, 'y'), (2, 'c'), (3, 'b'), (3, 'a')]
sorted() builtin: [(1, 'x'), (1, 'y'), (2, 'c'), (3, 'b'), (3, 'a')]
order matches: True
```

## How to check

`./check m04l01-06` copies `starter/` into a scratch directory and runs `python3 stability.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m04l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
