# m04l02-03 · Building the count array by hand

**Lesson:** [Counting And Radix Sort: Beating N Log N](https://learnsome.tech/learn/algorithms-course/m04l02) (lesson 4.2, module 4: Sorting And Searching) · Pro  
**Check:** Graded

## Goal

You can implement counting sort and LSD radix sort, explain when each applies, and describe the memory cost that comes with bypassing element comparisons.

In the lesson: Step through counting sort by hand in the Shell to see the count array before reconstruction. Assign a short list of digits and then allocate five zero counters for values zero through four. The single-line for loop does the filling the slots step: each value in data increments its own counter. Reading back the count array shows how many of each value appeared. The list comprehension in the fifth entry expands each counter into that many repetitions of its index, producing the sorted sequence. The final sorted call confirms the answer is identical. No element touched another element during the entire process: the sort ran on counts, not on comparisons. This is why the time cost grows with the range of keys and the number of elements, not with the relationship between them.

## Files

- [`starter/shell-building-the-count-array-by-hand.py`](starter/shell-building-the-count-array-by-hand.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l02/m04l02-03/starter`
2. Read `shell-building-the-count-array-by-hand.py`.
3. The session types these lines at the `>>>` prompt, in order:

   ```python
   data = [4, 2, 1, 4, 2, 3]
   counts = [0] * 5
   for v in data: counts[v] += 1
   counts
   [v for v in range(5) for _ in range(counts[v])]
   sorted(data)
   ```
4. Run it: `python3 -i < shell-building-the-count-array-by-hand.py`.
5. Check it from the repository root: `./check m04l02-03`.

## Expected output

```text
[0, 1, 2, 1, 2]
[1, 2, 2, 3, 4, 4]
[1, 2, 2, 3, 4, 4]
```

## How to check

`./check m04l02-03` copies `starter/` into a scratch directory and runs `python3 -i < shell-building-the-count-array-by-hand.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The session is typed into Python's interactive prompt line by line, as in the lesson, and what Python answers is compared with the answers recorded in the session (its `#   ` comment lines, collected into `expected.txt`): line by line, spaces at the end of a line and blank lines at the end do not count, and errors are compared with their traceback frames set aside. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m04l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
