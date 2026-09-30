# m01l05-03 · Fixed increment vs doubling: total copy cost

**Lesson:** [Amortised Analysis: Why Append Is Cheap](https://learnsome.tech/learn/algorithms-course/m01l05) (lesson 1.5, module 1: Complexity And Trade-offs) · Free  
**Check:** Graded

## Goal

You can explain why appending to a dynamic array is amortised constant time by tracing the doubling strategy, compare it to fixed-increment growth, and state the credit argument for the amortised bound.

In the lesson: The two functions simulate the two growth strategies without moving any data. The fixed increment function grows the capacity by four slots each time it fills. The doubling strategy function doubles the capacity each time it fills. Running both at sixteen, sixty-four, and two hundred and fifty-six appends shows the cost difference clearly. For sixteen appends, fixed copies twenty-four while doubling copies fifteen. For sixty-four, the fixed count jumps to four hundred and eighty while the doubling count stays at sixty-three. By two hundred and fifty-six, the third column shows doubling at two hundred and fifty-five while fixed has accumulated more than eight thousand copies. The fixed increment strategy pays quadratic total copy cost as n grows; the doubling strategy pays linear total cost.

## Files

- [`starter/compare_growth.py`](starter/compare_growth.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l05/m01l05-03/starter`
2. Read `compare_growth.py` the way the lesson builds it:
   - Lines 1–8: fixed increment
   - Lines 9–17: doubling strategy
   - Lines 18–20: third column
3. Run it: `python3 compare_growth.py`.
4. Check it from the repository root: `./check m01l05-03`.

## Expected output

```text
16 24 15
64 480 63
256 8064 255
```

## How to check

`./check m01l05-03` copies `starter/` into a scratch directory and runs `python3 compare_growth.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m01l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
