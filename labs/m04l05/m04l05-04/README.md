# m04l05-04 · Bisect as a sorted-list interface

**Lesson:** [Searching With Hashes Versus Trees](https://learnsome.tech/learn/algorithms-course/m04l05) (lesson 4.5, module 4: Sorting And Searching) · Pro  
**Check:** Graded

## Goal

You can choose between a set, a sorted list with bisect, and a linear scan for membership and range queries, and explain when sorted order provides capabilities that hashing cannot.

In the lesson: The bisect module gives you most of what a dedicated sorted-set data structure provides, using an ordinary list. Bisect-left on twenty-five in the list of multiples of ten returns two: the insertion point just past twenty, which is also where twenty-five would go to keep the list sorted. Bisect-right on thirty, which is actually present, returns three: one past the last thirty. After insort adds thirty-five the list grows to six elements with thirty-five in the correct position. The last entry combines both bisect calls for a range query: bisect-left of twenty-five finds where the window starts and bisect-right of forty-five finds where it ends, giving the slice containing thirty, thirty-five, and forty. This pattern works well as long as you mainly insert and search; if you also need frequent deletion, a plain list is not the right underlying container because deletion shifts elements.

## Files

- [`starter/shell-bisect-as-a-sorted-list-interface.py`](starter/shell-bisect-as-a-sorted-list-interface.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l05/m04l05-04/starter`
2. Read `shell-bisect-as-a-sorted-list-interface.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   import bisect
   a = [10, 20, 30, 40, 50]
   bisect.bisect_left(a, 25)
   bisect.bisect_right(a, 30)
   bisect.insort(a, 35)
   a
   a[bisect.bisect_left(a,25):bisect.bisect_right(a,45)]
   ```
4. Run it: `python3 -i < shell-bisect-as-a-sorted-list-interface.py`.
5. Check it from the repository root: `./check m04l05-04`.

## Expected output

```text
2
3
[10, 20, 30, 35, 40, 50]
[30, 35, 40]
```

## How to check

`./check m04l05-04` copies `starter/` into a scratch directory and runs `python3 -i < shell-bisect-as-a-sorted-list-interface.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m04l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
