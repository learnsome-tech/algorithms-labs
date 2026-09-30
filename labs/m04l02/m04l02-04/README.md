# m04l02-04 · LSD radix sort: sorting digit by digit

**Lesson:** [Counting And Radix Sort: Beating N Log N](https://learnsome.tech/learn/algorithms-course/m04l02) (lesson 4.2, module 4: Sorting And Searching) · Pro  
**Check:** Graded

## Goal

You can implement counting sort and LSD radix sort, explain when each applies, and describe the memory cost that comes with bypassing element comparisons.

In the lesson: LSD radix sort makes three passes over the data, one for each decimal digit position. In pass zero it sorts by the ones digit, in pass one by the tens digit, and in pass two by the hundreds digit. Each pass uses a bucket sort: it routes each value into one of ten buckets according to the current digit, then empties the buckets in order. The key property that makes this correct is stability: each bucket pass is stable, so elements with the same digit at the current position stay in the order that the previous pass established. After the units pass, elements sharing a units digit are in their input order. After the tens pass they are ordered by tens-and-units. After the final hundreds pass the full array is sorted. All three passes over the data cost linear time. The verified line confirms the result against the standard sort.

## Files

- [`starter/radix_sort.py`](starter/radix_sort.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l02/m04l02-04/starter`
2. Read `radix_sort.py` the way the lesson builds it:
   - Lines 1–11: three passes over the data
   - Lines 12–19: verified line confirms
3. Run it: `python3 radix_sort.py`.
4. Check it from the repository root: `./check m04l02-04`.

## Expected output

```text
input:  [137, 582, 867, 821, 782, 64, 261, 120, 507, 779]
sorted: [64, 120, 137, 261, 507, 582, 779, 782, 821, 867]
verified: True
```

## How to check

`./check m04l02-04` copies `starter/` into a scratch directory and runs `python3 radix_sort.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m04l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
