# m02l02-03 · Tracking load factor and signalling a resize

**Lesson:** [Hash Tables: Chaining, Open Addressing And Load Factor](https://learnsome.tech/learn/algorithms-course/m02l02) (lesson 2.2, module 2: Hashing: Structure Behind Everything Fast) · Pro  
**Check:** Graded

## Goal

You can implement a chaining hash map and a linear-probing open-addressed table, explain what the load factor measures, and identify when and why a table must resize.

In the lesson: Every insertion changes the load factor, and a well-built table monitors that number continuously. The slot helper produces a stable slot from the key. The load function divides item count by bucket count, and needs-resize returns true when that fraction exceeds seven tenths. Insert five words one at a time and watch the output panel. The first word loads the table to one quarter, safely below the threshold. The second word brings it to one half. The third word pushes it to three quarters: resize becomes true for all subsequent insertions. A real implementation would stop at this point, double the bucket count, and rehash every existing entry into the new, larger array. Catching the threshold at three quarters means chains stay short and most lookups still cost a single comparison at the right slot.

## Files

- [`starter/loadfactor.py`](starter/loadfactor.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l02/m02l02-03/starter`
2. Read `loadfactor.py` the way the lesson builds it:
   - Lines 1–4: stable slot
   - Lines 5–8: seven tenths
   - Lines 9–17: five words one at a time
3. Run it: `python3 loadfactor.py`.
4. Check it from the repository root: `./check m02l02-03`.

## Expected output

```text
red -> 2 | load 0.25 | resize? False
green -> 0 | load 0.5 | resize? False
blue -> 0 | load 0.75 | resize? True
gold -> 3 | load 1.0 | resize? True
pink -> 1 | load 1.25 | resize? True
```

## How to check

`./check m02l02-03` copies `starter/` into a scratch directory and runs `python3 loadfactor.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m02l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
