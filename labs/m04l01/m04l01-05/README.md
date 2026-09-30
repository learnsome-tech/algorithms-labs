# m04l01-05 · Comparison counts at three sizes

**Lesson:** [Comparison Sorts: Insertion, Merge And Quicksort](https://learnsome.tech/learn/algorithms-course/m04l01) (lesson 4.1, module 4: Sorting And Searching) · Pro  
**Check:** Graded

## Goal

You can implement insertion sort, merge sort, and quicksort with comparison counters, explain why no comparison sort beats order n log n, and demonstrate stability with tagged pairs.

In the lesson: All three algorithms now run on the same random data, re-seeded identically before each size so the comparison is perfectly fair. At ten elements the differences are small; the random data happens to favor insertion sort here. At fifty elements the quadratic nature of insertion sort becomes visible: six hundred fifteen comparisons against two hundred twenty-two for merge sort and two hundred fifty-three for quicksort. At one hundred elements, insertion sort costs over two thousand while the other two stay below seven hundred. The three rows appear and the ratio is stark: doubling n roughly quadruples insertion sort but only doubles the other two. The functional-style quicksort here counts each element-versus-pivot comparison by adding the subarray length minus one at each recursive call, which gives the exact element comparison count.

## Files

- [`starter/sort_compare.py`](starter/sort_compare.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l01/m04l01-05/starter`
2. Read `sort_compare.py`.
3. Run it: `python3 sort_compare.py`.
4. Check it from the repository root: `./check m04l01-05`.

## Expected output

```text
n=10: ins=19, mrg=25, qks=23
n=50: ins=615, mrg=222, qks=253
n=100: ins=2230, mrg=547, qks=656
```

## How to check

`./check m04l01-05` copies `starter/` into a scratch directory and runs `python3 sort_compare.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m04l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
