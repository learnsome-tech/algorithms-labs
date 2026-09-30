# m02l02-04 · Linear probing fills the next free slot

**Lesson:** [Hash Tables: Chaining, Open Addressing And Load Factor](https://learnsome.tech/learn/algorithms-course/m02l02) (lesson 2.2, module 2: Hashing: Structure Behind Everything Fast) · Pro  
**Check:** Graded

## Goal

You can implement a chaining hash map and a linear-probing open-addressed table, explain what the load factor measures, and identify when and why a table must resize.

In the lesson: Open addressing resolves collisions by scanning forward through the array. The function computes a starting slot from the key's hash, then increments until it finds an empty cell or a matching key. A tombstone marks deleted slots, which is a sentinel distinct from empty: if you replaced a deleted entry with plain empty, any lookup for a key that was inserted through that slot would stop too early and miss. Insert six integer keys that are deliberately chosen to collide: three, eleven, and nineteen all hash to slot three modulo eight, so the second and third arrivals probe forward. Six insertions into an eight-slot table cost a total probes of ten rather than the ideal six: those four extra probes are the cost of the clustering. The load factor is six eighths, right at the threshold where resizing pays off.

## Files

- [`starter/linprobe.py`](starter/linprobe.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l02/m02l02-04/starter`
2. Read `linprobe.py` the way the lesson builds it:
   - Lines 1–11: tombstone marks deleted slots
   - Lines 12–19: six integer keys
3. Run it: `python3 linprobe.py`.
4. Check it from the repository root: `./check m02l02-04`.

## Expected output

```text
total probes: 10
load: 6 / 8
```

## How to check

`./check m02l02-04` copies `starter/` into a scratch directory and runs `python3 linprobe.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/algorithms-course/m02l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
